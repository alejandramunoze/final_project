# final_project
Improvement on Hoya Hunters' Housing Search

## Get an Google Maps API Key 
For this website you need to retrieve a Google Maps API Key. It has a maximum of $200 credit per month

To get one do the following:
1. Go to https://console.cloud.google.com/
2. Create a new project or select an existing one
3. Enable the "Street View Image API" for your project
4. Create API credentials (an API key) (you will need to input a credit card)

Remember to store the API key in a secret location

## Version 1
In this first version, we built on from the website that we created in class. We added a navigation link to a new route (/house) which would show a predetermined street view image captured.

## Google Spreadsheet Access:
Same as with the Google Maps API, remember to download the .json credentials of your service account from your Google Cloud system

## To run the app:

conda activate my-first-env

pip install -r requirements.txt

export FLASK_APP=website_app

flask run 

