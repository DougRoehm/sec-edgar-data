# High level summary of EDGAR information available for company
import requests
from edgar_functions import get_cik, get_submissions, get_company_facts
from headers import headers

print("This program provides a high level overview of EDGAR data available for a company.")
ticker = input("Enter Company Ticker: ")
print(f"Company ticker: {ticker}")

cik = get_cik(ticker, headers=headers)
print(f"Company CIK Number: {cik}")

submissions = get_submissions(cik, headers=headers)
print("Submissions information available:")
print(submissions.keys())

company_facts = get_company_facts(cik, headers=headers)
print("Company facts information available:")
print(company_facts.keys())

print("End Program")
