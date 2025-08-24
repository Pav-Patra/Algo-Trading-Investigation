from pyfinance import TSeries # pyfinance is a python library for quantative analysis on financial data
import yfinance as yf
import argparse
import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame
from datetime import datetime, time, timedelta
from backports.zoneinfo import ZoneInfo
import plotly.tools as tls
import plotly.io as pio
from curl_cffi import requests


"""
asset_load.py - a series of functions that manipulates and normalises data using pandas. 
Data is fetched from yfinance.

by Pav Patra, a dictionary stores, for each asset, {asset_code : asset_full_name}

select stocks/funds/etfs are used for now

"""



matplotlib.use('agg')
logger = logging.getLogger(__name__)

session = requests.Session(impersonate="chrome")

# select asset list
ETF_LIST = {
    '0P0000TKZK.L': 'Vanguard_LifeStrategy_60_Equity_Acc',
    '0P0000TKZM.L': 'Vanguard_LifeStrategy_80_Equity_Acc',
    '0P0000KSP6.L': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc',
    '0P000185T3.L': 'Vanguard_Global_Equity_Accumulation',
    'VERE.MI': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation',
    'VMID.SW': 'Vanguard FTSE 250 UCITS ETF',
    'PLTR': 'Palantir Technologies Inc.',
    'NVDA': 'NVIDIA Corporation',
    'MSFT': 'Microsoft Corporation',
    'GOOG': 'Alphabet Inc.'
}


EXCHANGE_HOURS = {
    "NMS": {  # NASDAQ (New York, Eastern Time)
        "open": time(9, 30),  # ET
        "close": time(16, 00)
    },
    "NYQ": {  # NYSE (New York, Eastern Time)
        "open": time(9, 30),  # ET
        "close": time(16, 00)
    },
    "LSE": {  # London Stock Exchange (UK Time)
        "open": time(8, 00),  # BST or GMT depending on DST
        "close": time(16, 30)
    },
    "HKG": {  # Hong Kong (Hong Kong Time)
        "open": "09:30",  # HKT
        "close": "16:00"
    },
    "TSE": {  # Tokyo Stock Exchange (Japan Time)
        "open": "09:00",  # JST
        "close": "15:00"
    },
}


def select_asset(asset_code: str):
    asset_data = yf.Ticker(asset_code, session=session)

    logger.info(asset_data.info)

    historical_data = asset_data.history(period="1y")

    logger.info("Historical past year data:")
    logger.info(historical_data)

    return historical_data


def select_asset_x_years(asset_code: str, years: int):
    asset_data = yf.Ticker(asset_code, session=session)

    historical_data = asset_data.history(period=f"{years}y")

    logger.info(f"Historical data for past {years} years:")
    # logger.info(historical_data)

    return historical_data


def select_asset_all_history(asset_code: str):
    asset_data = yf.Ticker(asset_code, session=session)

    return asset_data.history(period="max")


def get_asset_info(asset_code: str):
    print(asset_code)
    asset_data = yf.Ticker(asset_code, session=session)
    print(asset_data)
    return asset_data.get_info()


def get_close_price_list_with_date(asset_data: DataFrame):
    return asset_data['Close']

def timestamp_to_date(given_date: datetime):
    return datetime.strftime(given_date, '%d-%m-%Y')


def draw_line_graph(asset_data: DataFrame, asset_name: str):
    current_frame = asset_data
    
    try:
        current_frame['formatted_date'] = current_frame.index.date
    except Exception as e:
        logger.error(f"Supplied index for asset data frame {asset_data.iloc[0].name} was invalid for conversion to formatted Date")
        logger.error(e)


    # logger.info(current_frame['formatted_date'])
    # logger.info(current_frame['Close'])

    fig = plt.figure()
    plt.title(asset_name)
    plt.xlabel("formatted_date")
    plt.ylabel("Close")
    plt.plot(current_frame['formatted_date'], current_frame['Close'])
    

    return fig


def get_asset_close_data(asset: str) -> list:
    """
    Fetches, for a given asset name, the all-time history of close prices as a list
    of close date and close price pairs.

    Args:
        asset (str): the asset name

    Returns:
        asset_date_close_list ([str, int]): list of close date close price pairs 

    """

    logger.info(f"Selected asset: {asset}")
    asset_data = select_asset_all_history(asset)

    logger.info(asset_data)

    current_frame = asset_data

    try:
        current_frame['formatted_data'] = current_frame.index.date
        
    except Exception as e:
        logger.error(f"Supplied index for asset data frame {asset_data.iloc[0].name} was invalid for conversion to formatted Date")
        logger.error(e)

    # logger.info(current_frame['formatted_date'])
    # logger.info(current_frame['Close'])

    logger.info(current_frame.index.date)
    logger.info(len(current_frame.index.date))
    logger.info(len(current_frame['Close']))

    return [current_frame.index.date, current_frame['Close']]


def get_market_hours(ticker_str):
    ticker = yf.Ticker(ticker_str)
    exchange = ticker.info.get("exchange")
    hours = EXCHANGE_HOURS.get(exchange)
    if hours:
        return {
            "exchange": exchange,
            "open": hours["open"],
            "close": hours["close"]
        }
    else:
        return {
            "exchange": exchange or "Unknown",
            "open": "Unknown",
            "close": "Unknown"
        }
    
def is_weekday(day: int):
    '''
    Takes a day of the week where 0 references Monday and 6 references Sunday

    Args:
        day (int): day of the week

    Returns: 
        days < 5 (boolean): expression to determine whether day is a week day
    '''
    return day < 5


def get_calc_date_time(asset):
    exchange = get_market_hours(asset)['exchange']

    if exchange == 'NMS' or exchange == 'NYQ':
        datetime_utc = datetime.now()
        return datetime_utc.astimezone(ZoneInfo("America/New_York"))
    elif exchange == 'HKG':
        datetime_utc = datetime.now()
        return datetime_utc.astimezone(ZoneInfo("Asia/Hong_Kong"))
    elif exchange == 'TSE':
        datetime_utc = datetime.now()
        return datetime_utc.astimezone(ZoneInfo("Asia/Tokyo"))
    else:
        return datetime.now()



def calc_last_close_price(asset_hours: dict, calc_date_time: datetime):
    logger.info(f"day of the week: {calc_date_time.weekday()}")

    if calc_date_time.weekday() > 4 or (calc_date_time.weekday == 0 and calc_date_time.time() < asset_hours['open']):
        days_since_friday = (calc_date_time.weekday() - 4) % 7
        last_close_date = (calc_date_time - timedelta(days=days_since_friday)).date()
        return datetime.combine(last_close_date, asset_hours['close'])

    elif calc_date_time.time() > asset_hours['close']:
        return datetime.combine(calc_date_time.date(), asset_hours['close'])
    else:
        logger.info(f"Calculated time: {asset_hours['close']}")
        last_close_date = (calc_date_time - timedelta(days=calc_date_time.weekday()-1)).date()
        logger.info(f"Calculated date: {last_close_date}")
        return datetime.combine(last_close_date, asset_hours['close'])



def get_stock_close_price(asset: str, minutes: int):
    """
    Returns the change in price for an asset from current time back to a time specified in minutes
    """

    # given a time in minutes, get the close price at date time calculated by subtracting time given from current time

    # logic only works if ticker.info["quoteType"] == Equite, mutual funds and ETFs do not have by minute close prices - look at open per day

    ticker = yf.Ticker(asset, session=session)

    current_time = get_calc_date_time(asset)

    calc_date_time = current_time - timedelta(minutes=float(minutes))

    date_time_thirty = current_time - timedelta(days=float(30))

    end_time = 0

    logger.info(f"Calc date time: {calc_date_time}")
    logger.info(f"Thirty date time: {date_time_thirty}")
    logger.info(f"Calc time type: {type(calc_date_time.time())}")

    asset_hours = get_market_hours(asset)

    logger.info(f"open time type: {type(asset_hours['open'])}")

    logger.info(f"asset_hours: {asset_hours}")

    close_price_at_time = None

    if calc_date_time > date_time_thirty:
        # for minute spans, if weekday, get close price of previous day if < opend time, else get close price on same day if > close time
        # if weekend, get close price on friday
        if is_weekday(calc_date_time.weekday()) and calc_date_time.time() >= asset_hours['open'] and calc_date_time.time() <= asset_hours['close']:

            logger.info("Less than thrirty days")
            end_time = calc_date_time + timedelta(minutes=float(1))

            asset_price = ticker.history(start=calc_date_time, end=end_time, interval="1m")

            
            close_price_at_time = asset_price['Close'][0]
        
        else:
            # worst case stated calc time is Monday at 8:59am
            # solution go back by 2 and half days days with 1m intervals
            # if weekday is saturday or sunday or before monday open get close price from last friday
            # if weekday and not monday but time is before open get price of close from previous day
            # if weekday and time after close get price at close on same day


            logger.info(f"No available price for given time frame {calc_date_time.weekday()} at {calc_date_time.time()}")

            end_time = calc_last_close_price(asset_hours, calc_date_time)
            logger.info(f"adjusted close time: {calc_date_time}")
            calc_date_time = end_time - timedelta(minutes=1)
            asset_price = ticker.history(start=calc_date_time, end=end_time, interval="1m")

            close_price_at_time = asset_price['Close'][0]

            

    else:
        # for day spans, if outside trading hours (saturday/sunday) get close on friday

        logger.info("More than thrirty days")
        end_time = calc_date_time + timedelta(days=float(1))

        calc_day = calc_date_time.weekday()
        logger.info(f"weekday: {calc_day}")

        if is_weekday(calc_day):
            logger.info(f"{calc_day} is a trading day")

            asset_price = ticker.history(start=calc_date_time, end=end_time, interval="1d")
            close_price_at_time = asset_price['Close'][0]
        else:
            logger.info(f"{calc_day} is not a trading day at {calc_date_time.day}")
            calc_date_time = calc_last_close_price(asset_hours, calc_date_time)
            logger.info(f"adjusted close time: {calc_date_time}")
            end_time = calc_date_time + timedelta(days=float(1))

            asset_price = ticker.history(start=calc_date_time, end=end_time, interval="1d")
            close_price_at_time = asset_price['Close'][0]


    logger.info(f"Calculated start time for {asset}: {calc_date_time}")
    logger.info(f"Calculated end time for {asset}: {end_time}")

    if close_price_at_time is not None:
        logger.info(f"Close price at time: {close_price_at_time}")
        return close_price_at_time

    # use calculated_price_at_time to find the percentage difference between this time and
    # the time of the last close price and return this
    # also handle the issue with mutual funds and ETF which don't supply per minute data 


def get_asset_change_price(asset: str, minutes: int):
    """
    Returns the percentager change in price of an asset between current time and x minutes ago
    """

    ticker = yf.Ticker(asset, session=session)

    if ticker.info["quoteType"] == "EQUITY":
        latest_close_price = get_stock_close_price(asset, 0)
        previous_close_price = get_stock_close_price(asset, minutes)

        percentage_change = ((latest_close_price - previous_close_price) / previous_close_price) * 100

        logger.info(f"Percentage change close price: {percentage_change}")
        return percentage_change
    else:
        raise Exception(f"Asset: {asset} does not support percentage change per minute calulation")



    
    



def render_graph_html(asset):
    logger.info(f"Selected asset: {asset}")
    asset_info = get_asset_info(asset)
    asset_long_name = asset_info['longName']
    logger.info(asset_long_name)

    logger.info("All time market data:")

    max_history_data = select_asset_all_history(asset)
    # logger.info(max_history_data.iloc[0])

    # logger.info(f"Asset close prices: {get_close_price_list_with_date(max_history_data)}")
    logger.info(f"Total number of prices: {len(max_history_data['Close'])}")
    fig = draw_line_graph(max_history_data, asset_long_name)

    # convert matplot to Plotly
    plotly_fig = tls.mpl_to_plotly(fig)

    html_str = pio.to_html(plotly_fig, full_html=False, include_plotlyjs='cdn')

    return html_str
    







if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

#     for asset in ETF_LIST:
#         asset_info = get_asset_info(asset)

#         asset_long_name = asset_info['longName']

#         logger.info(asset_long_name)

#         logger.info("All time market data:")

#         max_history_data = select_asset_all_history(asset)
#         logger.info(max_history_data.iloc[0])

#         logger.info(f"Asset close prices: {get_close_price_list_with_date(max_history_data)}")
#         logger.info(f"Total number of prices: {len(max_history_data['Close'])}")
#         draw_line_graph(max_history_data, asset_long_name)
#         render_graph_html(asset)
#         logger.info("--------------------------------------")
    get_asset_change_price('PLTR',80200)
    get_asset_change_price('PLTR',1840)

    # get_percentage_change_stock('PLTR',842)

    # ticker = yf.Ticker('PLTR', session=session)

    # ticker_history = ticker.history(start= datetime(2025, 7, 10, 0, 1), end=datetime(2025, 7, 10, 23, 58), interval="1m")
    # logger.info(ticker_history.index.tz)
    # logger.info(ticker.info["quoteType"])
    # logger.info(ticker_history)