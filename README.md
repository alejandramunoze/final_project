# final_project
Improvement on Hoya Hunters' Housing Search

## Get an Google API Keys
For this website you need to retrieve a Google Maps API Key. It has a maximum of $200 credit per month

To get one do the following:
1. Go to https://console.cloud.google.com/
2. Create a new project or select an existing one
3. Enable the "Street View Image API", "Geocoding API" and "Google Sheets API" for your project
4. Create API credentials (an API key) (you will need to input a credit card)
5. You will also need the "credentials.json" file by having a service account in that same project, for the use of Geolocation.

Remember to store the API key and credentials in a secret location.

## Set Up
Create and activate a virtual environment:

conda create -n my-first-env python=3.10

conda activate my-first-env

Install packages:

pip install -r requirements.txt


Create a ".env" file and paste in the following contents:

# this is the ".env" file...
GOOGLE_MAPS_API = "____________" 
SPREADSHEET_URL = (example)'https://docs.google.com/spreadsheets/____________________'

# this is the credentials.json file...
{
    "type": "service_account",
    "project_id": "__________",
    "private_key_id": "________",
    "private_key": "-----BEGIN PRIVATE KEY-----\_________________\n-----END PRIVATE KEY-----\n",
    "client_email": "sth@project-name.iam.gserviceaccount.com",
    "client_id": "______________",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/project_name_example.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
  }


## Usage
One can use any of the functions (spreadsheet reading, street_view image retrieving and coordinates by address) by invoking the file:
python -m app.spreadsheet
python -m app.street_view


## Website Creation
In this project we built on from the website that we created in class. Utilizing the home_routes.py file and the bootstrap template layout 5 we can find the "skeleton" for our site. 

We have four main navigation links: 
- (/) and (/about) which will reference the main page.
- (/add_houses) which connects the Google Form to the website, where users can add their own houses and information onto the spreadsheet.
- (/form) which hosts the website form to filter through the data.
- (/filter) which then gives the results from the filtering following the inputted website form.


## To run the app:
Run the web app (then view in the browser at http://localhost:5000/):

# First -
conda activate my-first-env
pip install -r requirements.txt

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run


## Testing
To run tests:
pytest