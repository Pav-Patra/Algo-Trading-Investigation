from pyfinance import TSeries # pyfinance is a python library for quantative analysis on financial data
import yfinance as yf
import argparse
import numpy as np
import pandas as pd


np.random.seed(444)

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

    print(asset_data.info)

    print("start date:")
    try:
        print(asset_data.info['startDate'])
    except:
        print("asset does not have start date")

    historical_data = asset_data.history(period="1y")
    print("Historical past year data:")
    print(historical_data)

def example_yfinance():
    # Define the ticker symbol
    ticker_symbol = "AAPL"

    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # Fetch historical market data
    historical_data = ticker.history(period="1y")  # data for the last year
    print("Historical Data:")
    print(historical_data)

    # Fetch basic financials
    financials = ticker.financials
    print("\nFinancials:")
    print(financials)

    # Fetch stock actions like dividends and splits
    actions = ticker.actions
    print("\nStock Actions:")
    print(actions)


if __name__ == "__main__":
    for asset in etf_list:
        print(asset)

        select_asset(asset)
        