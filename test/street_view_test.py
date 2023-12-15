



# this is the "test/street_view_test.py" file...
import os 
import requests
import pandas as pd
from app.street_view import get_street_view_image, get_coordinates
from dotenv import load_dotenv
load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...
api_key = os.getenv("GOOGLE_MAPS_API")

def test_get_street_view_image():

    location = "38.907596, -77.071934"
    url = get_street_view_image(api_key, location)
    # Check if the URL is not None and that it corresponds to the previous sample coordinates
    assert url is not None
    assert url == f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location=38.907596%2C+-77.071934&fov=90&heading=0&pitch=0&key={api_key}'

    # Check if the URL is a string
    assert isinstance(url, str)

    # Check if the URL is valid by making a request
    response = requests.get(url)
    assert response.status_code == 200

    
def test_get_coordinates():
    address = "3700 O St NW Washington DC"
    coordinates = get_coordinates(api_key, address)

    # Check if coordinates are not None
    assert coordinates is not None
    assert coordinates == "38.907596, -77.071934"

    # Check if coordinates are a string
    assert isinstance(coordinates, str)

    # Check if coordinates are in the expected format "latitude, longitude"
    assert "," in coordinates

    # Check if coordinates can be converted to floats
    latitude, longitude = map(float, coordinates.split(","))
    
    # Check if latitude and longitude are within valid ranges
    assert -90 <= latitude <= 90
    assert -180 <= longitude <= 180


