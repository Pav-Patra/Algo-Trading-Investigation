from pyfinance import TSeries
import argparse
import numpy as np
import pandas as pd


np.random.seed(444)

etf_list = [
    '0P0000TKZK.L',
    '0P0000TKZM.L',
    '0P0000KSP6.L',
    '0P000185T3.L',
    'VERE.M',
    'VMID.SW'
]

def random_stock():
    s = np.random.randn(400) / 100 + 0.008
    idx = pd.date_range(start='2016', periods=len(s))
    ts = TSeries(s, index=idx)

    return ts


if __name__ == "__main__":
    stock_select = random_stock()
    print(stock_select.head())