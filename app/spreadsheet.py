# imports at top
import os
import pandas as pd
import gspread
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# Authenticate with google
gc = gspread.service_account(filename="app\credentials.json")
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")


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