# imports at top
import os
import pandas as pd
import gspread
from pprint import pprint


# Authenticate with google
gc = gspread.service_account(filename="app\credentials.json")

# Get the URL
SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1-NdNLEbaHBToP3eG_dBDNKhYcFeRkDTlwn0-_dK10Zs/edit?usp=sharing'

def fetch_spreadsheet(spreadsheet_url=SPREADSHEET_URL):
    # Open spreadsheet
    workbook = gc.open_by_url(spreadsheet_url)
    sheet = workbook.sheet1  # or workbook.worksheet('SheetName') to access different sheet

    # Read data into a Pandas Data Frame
    data = sheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)


    return df



if __name__ == "__main__":

    
    df = fetch_spreadsheet()

    breakpoint()