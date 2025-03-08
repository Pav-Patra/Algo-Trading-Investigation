from pyfinance import TSeries # pyfinance is a python library for quantative analysis on financial data
import yfinance as yf
import argparse
import numpy as np
import pandas as pd
import logging



logger = logging.getLogger("load_etf")



etf_list = {
    '0P0000TKZK.L': 'Vanguard_LifeStrategy_60_Equity_Acc',
    '0P0000TKZM.L': 'Vanguard_LifeStrategy_80_Equity_Acc',
    '0P0000KSP6.L': 'Vanguard_FTSE_Dev_Wld_ex-UK_Eq_Idx_Acc',
    '0P000185T3.L': 'Vanguard_Global_Equity_Accumulation',
    'VERE.MI': 'Vanguard_FTSE_Developed_Europe_ex UK_UCITS_ETF_Accuimulation',
    'VMID.SW': 'Vanguard FTSE 250 UCITS ETF'
}



def select_asset(asset_code: str):
    asset_data = yf.Ticker(asset_code)

    logger.info(asset_data.info)

    historical_data = asset_data.history(period="1y")

    logger.info("Historical past year data:")
    logger.info(historical_data)

    return historical_data


def select_asset_x_years(asset_code: str, years: int):
    asset_data = yf.Ticker(asset_code)

    historical_data = asset_data.history(period=f"{years}y")

    logger.info(f"Historical data for past {years} years:")
    logger.info(historical_data)

    return historical_data


def select_asset_all_history(asset_code: str):
    asset_data = yf.Ticker(asset_code)

    return asset_data.history(period="max")


def get_asset_info(asset_code: str):
    asset_data = yf.Ticker(asset_code)
    return asset_data.info






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    for asset in etf_list:
        asset_info = get_asset_info(asset)

        asset_long_name = asset_info['longName']

        logger.info(asset_long_name)

        logger.info("All time market data:")

        max_history_data = select_asset_all_history(asset)
        logger.info(max_history_data.iloc[0])

        