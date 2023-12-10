# imports at top
import pandas as pd
import gspread
# from gspread import colab
# from colab import auth
# from auth import default

# Authenticate with google
gc = gspread.service_account(filename='path/to/your/service-account.json')
# auth.authenticate_user()
# creds, _ = default()
# gc = gspread.authorize(creds)

# Open spreadsheet
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1ihMA58RqFH2srdeGEne3sY4-xjhbKmU0XVdsWbs_gKY/edit#gid=0'
workbook = gc.open_by_url(spreadsheet_url)
sheet = workbook.sheet1  # or workbook.worksheet('SheetName') to access different sheet

# Read data into a Pandas Data Frame
data = sheet.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

# Preview Data Frame
print(df.head())

# Convert to DataFrame for easier handling
df = pd.DataFrame(data[1:], columns=data[0])

# Display data
print(type(df))
print(df.columns.tolist())

# EG print first row:
print("ROW #1:")
pprint(df.iloc[0].to_dict())