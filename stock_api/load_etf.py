from pyfinance import TSeries # pyfinance is a python library for quantative analysis on financial data
import yfinance as yf
import argparse
import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame
from datetime import datetime
import plotly.tools as tls
import plotly.io as pio
from curl_cffi import requests


# matplotlib.use('TkAgg')
logger = logging.getLogger("load_etf")

session = requests.Session(impersonate="chrome")

etf_list = {
    '0P0000TKZK.L': 'Vanguard_LifeStrategy_60_Equity_Acc',
    '0P0000TKZM.L': 'Vanguard_LifeStrategy_80_Equity_Acc',
    '0P0000KSP6.L': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc',
    '0P000185T3.L': 'Vanguard_Global_Equity_Accumulation',
    'VERE.MI': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation',
    'VMID.SW': 'Vanguard FTSE 250 UCITS ETF'
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
    logger.info(historical_data)

    return historical_data


def select_asset_all_history(asset_code: str):
    asset_data = yf.Ticker(asset_code, session=session)

    return asset_data.history(period="max")


def get_asset_info(asset_code: str):
    asset_data = yf.Ticker(asset_code, session=session)
    return asset_data.info


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


    logger.info(current_frame['formatted_date'])
    logger.info(current_frame['Close'])

    fig = plt.figure()
    plt.title(asset_name)
    plt.xlabel("formatted_date")
    plt.ylabel("Close")
    plt.plot(current_frame['formatted_date'], current_frame['Close'])
    

    return fig


def render_graph_html(asset):
    logger.info(f"Selected asset: {asset}")
    asset_info = get_asset_info(asset)
    asset_long_name = asset_info['longName']
    logger.info(asset_long_name)

    logger.info("All time market data:")

    max_history_data = select_asset_all_history(asset)
    logger.info(max_history_data.iloc[0])

    logger.info(f"Asset close prices: {get_close_price_list_with_date(max_history_data)}")
    logger.info(f"Total number of prices: {len(max_history_data['Close'])}")
    fig = draw_line_graph(max_history_data, asset_long_name)

    # convert matplot to Plotly
    plotly_fig = tls.mpl_to_plotly(fig)

    html_str = pio.to_html(plotly_fig, full_html=False, include_plotlyjs='cdn')

    return html_str
    







# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)

#     for asset in etf_list:
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
        