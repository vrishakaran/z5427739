""" yf_example3.py

Example of a function to download Qantas stock prices from Yahoo Finance for a specific year.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):

    """ Qantas prices from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------

    start: Download from start date string (YYYY-MM-DD) from 'year-01-01'

    end: Download ends at date string (YYYY-MM-DD) on 'year-12-21'
    """
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year+1}-01-01'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    return yf_example2.yf_prc_to_csv(tic, pth, start, end)

if __name__ == "__main__":
    qan_prc_to_csv(2020)



