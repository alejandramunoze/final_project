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
```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Install packages:
```sh
pip install -r requirements.txt
```

Create a ".env" file and paste in the following contents:

### this is the ".env" file...
```sh
GOOGLE_MAPS_API = "____________" 

SPREADSHEET_URL = (example)'https://docs.google.com/spreadsheets/____________________'
```
For the above "SPREADSHEET_URL" used in this Housing Platform, contact atm92@georgetown.edu.


### this is the credentials.json file...
```sh
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
```

In order to render the website later, this repository contains modifications of the above .json file in order to facilitate its codification and none disclosure. For that, we will store in the .env file the information from the credentials.json file:

```sh
PRIVATE_KEY_ID = "___combination of numbers and letters___"
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----...............\n-----END PRIVATE KEY-----\n"
CLIENT_ID = "___list of numbers___"
```


## Usage

One can use any of the functions (spreadsheet reading, street_view image retrieving and coordinates by address) by invoking the file:
```sh
python -m app.spreadsheet

python -m app.street_view
```

## Website Creation

In this project we built on from the website that we created in class. Utilizing the home_routes.py file and the bootstrap template layout 5 we can find the "skeleton" for our site. 

We have four main navigation links: 
- (/) and (/about) which will reference the main page.
- (/add_houses) which connects the Google Form to the website, where users can add their own houses and information onto the spreadsheet.
- (/form) which hosts the website form to filter through the data.
- (/filter) which then gives the results from the filtering following the inputted website form.


## Google Spreadsheet Access:
Same as with the Google Maps API, remember to download the .json credentials of your service account from your Google Cloud system

## To run the app:

Run the web app (then view in the browser at http://localhost:5000/):

### First -
```sh
conda activate my-first-env

pip install -r requirements.txt
```

### Mac OS:
```sh
FLASK_APP=web_app flask run
```

### Windows OS:
#### ... if `export` doesn't work for you, try `set` instead
#### ... or set FLASK_APP variable via ".env" file
```sh
export FLASK_APP=web_app
flask run
```

## Testing
To run tests:
```sh
pytest
```

