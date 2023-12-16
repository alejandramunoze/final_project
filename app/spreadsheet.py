'''
# imports at top
import os
import pandas as pd 
import gspread
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# Authenticate with google
DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)


gc = gspread.service_account(filename=GOOGLE_CREDENTIALS_FILEPATH)
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

    headers = df.columns.tolist()
    print(headers)

    print(type(df[0]))
    print(len(df))


    breakpoint()

'''
import os
import pandas as pd
import gspread
from dotenv import load_dotenv
import json
import base64

load_dotenv()

# Function to load credentials from environment variables
def load_credentials():
    try:
        print("Loading credentials from environment variables")
        client_id = os.environ.get("CLIENT_ID")
        private_key = os.environ.get("PRIVATE_KEY")
        private_key_id = os.environ.get("PRIVATE_KEY_ID")

        credentials = {
            "type": "service_account",
            "project_id": "mgmt-for-python-project",
            "private_key_id": private_key_id,
            "private_key": private_key.replace("\\n", "\n"),  # Replace escaped newlines
            "client_email": "hoya-housing-seniors@mgmt-for-python-project.iam.gserviceaccount.com",
            "client_id": client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/your-client-email%40your-project.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }

        print("Credentials loaded successfully.")
        return credentials
    except Exception as e:
        print(f"Error loading credentials from environment variables: {e}")
        return None

# Function to encode credentials to base64
def encode_credentials(credentials):
    try:
        credentials_str = json.dumps(credentials)
        encoded_credentials = base64.b64encode(credentials_str.encode()).decode()
        print("Credentials encoded successfully.")
        return encoded_credentials
    except Exception as e:
        print(f"Error encoding credentials: {e}")
        return None

# Function to save credentials to a file in JSON format
def save_credentials_to_file(credentials, filepath="encoded_credentials.json"):
    try:
        with open(filepath, "w") as file:
            json.dump(credentials, file)
        print(f"Credentials saved to {filepath}")
    except Exception as e:
        print(f"Error saving credentials to file: {e}")



# Load credentials and encode them
credentials = load_credentials()
if credentials:
    save_credentials_to_file(credentials)  # Save credentials to a JSON file
    encoded_credentials = encode_credentials(credentials)
    if encoded_credentials:
        gc = gspread.service_account(filename="encoded_credentials.json")  # Use the JSON file
        print("Authenticated with Google successfully.")
    else:
        print("Failed to encode credentials.")
else:
    print("Failed to load credentials.")


SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")

def fetch_spreadsheet(spreadsheet_url=SPREADSHEET_URL):
    # Open spreadsheet
    workbook = gc.open_by_url(spreadsheet_url)
    sheet = workbook.sheet1  # or workbook.worksheet('SheetName') to access a different sheet

    # Read data into a Pandas Data Frame
    data = sheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)

    return df

if __name__ == "__main__":
    df = fetch_spreadsheet()

    headers = df.columns.tolist()
    print(headers)

    print(type(df.iloc[0]))
    print(len(df))

    breakpoint()
