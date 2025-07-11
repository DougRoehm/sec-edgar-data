# edgar_functions
import requests
from headers import headers

def get_cik(ticker, headers=headers):
    """
    Use a public traded companies tikcer to get their CIK number.

    A CIK number, or Central Index Key, is a unique 10-digit \n
    identifier assigned by the SEC to companies. This CIK is needed to \n
    access data using the SEC EDGAR API.

    Parameters:
        ticker (str): The ticker for the company to get CIK number.
        headers=headers (dictionary): Contains the API required header \n
        identifying the user.

    Returns:
        cik (str): String of the cik number.

    Raises:
        ValueError: If ticker not in API database.

    """
    link = "https://www.sec.gov/files/company_tickers.json"
    ticker = ticker.upper().replace(".", "-")
    ticker_json = requests.get(link, headers=headers).json()

    for company in ticker_json.values():
        if company["ticker"] == ticker:
            cik = str(company["cik_str"]).zfill(10)
            return cik
    
    raise ValueError(f"Ticker {ticker} not found in SEC database")


def get_submissions(cik, headers=headers):
    """ 
    Returns EDGAR submissions data for supplied cik number 

    Uses a companies CIK number to pully company data from EDGARs \n
    submissions API.

    Parameters:
        cik (str): String of cik number
        headers=headers (dict): A dictionary containing information \n
        identifying the person requesting the data (Name and Email)

    Returns:
        submission (dict): As JSON object
    
    """
    url = f"https://data.sec.gov/submissions/CIK{str(cik).zfill(10)}.json"
    return requests.get(url, headers=headers).json()


def get_company_facts(cik, headers=headers):
    """ 
    Returns company facts from EDGAR company-concept API

    Uses a companies CIK number to pully company data from EDGARs \n
    company-concep API.

    Parameters:
        cik (str): String of cik number
        headers=headers (dict): A dictionary containing information \n
        identifying the person requesting the data (Name and Email)

    Returns:
        company facts (dict): As JSON object
    
    """
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik).zfill(10)}.json"
    return requests.get(url, headers=headers).json()

