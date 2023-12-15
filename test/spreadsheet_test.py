


# this is the "test/spreadsheet_test.py" file...

import pandas as pd
from app.spreadsheet import fetch_spreadsheet

def test_fetch_spreadsheet():
    df = fetch_spreadsheet()
    # Check it has correctly read the titles of the columns
    assert df.columns.tolist() == ['Timestamp', 'Email Address', 'address', 'neighborhood', 'type', 'apt-num', 'single-num', 'double-num', 'bathroom-num', 'patio', 'parking', 'rent', 'landlord', 'phone', 'email', 'comments', 'Capacity']
    # Check lenth of df is correct
    assert len(df) > 300
    # Check if df is a DataFrame
    assert isinstance(df, pd.DataFrame)
    # Check if the first column (df[0]) can be converted to a dictionary
    assert isinstance(df.iloc[0].to_dict(), dict)


