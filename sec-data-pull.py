# Program to pull data from SEC database using SEC Edgar API

import pandas as pd
import requests
from headers import headers

def main():

    # List of tickers to pull cik
    tickers = ["AEE", "AEP", "AVA", "BKH", "CMS", "CNP", "DTE", "ETR", "EVRG", "IDA", "LNT",
          "MGEE", "NWE", "OGE", "POR", "WEC"]
    
    # Create dictionary for capturing cik data
    cik_dict = {}

    for ticker in tickers:
        cik = cik_matching_ticker(ticker)
        # print(cik)
        cik_dict[ticker] = cik
        
    print(cik_dict)
    print("Done")

    # TODO use cik to pull financial data

def cik_matching_ticker(ticker, headers=headers):
    link = "https://www.sec.gov/files/company_tickers.json"
    ticker = ticker.upper().replace(".", "-")
    ticker_json = requests.get(link, headers=headers).json()

    for company in ticker_json.values():
        if company["ticker"] == ticker:
            cik = str(company["cik_str"]).zfill(10)
            return cik
    raise ValueError(f"Ticker {ticker} not found in SEC database")


if __name__ == "__main__":
    main()