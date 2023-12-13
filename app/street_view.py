
# street_view.py

import os 
import requests
from dotenv import load_dotenv
load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...
api_key = os.getenv("GOOGLE_MAPS_API")
meta_base = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
 


def get_street_view_image(api_key, location, size="600x300", fov=90, heading=0, pitch=0):
    base_url = "https://maps.googleapis.com/maps/api/streetview?"
    params = {
        "size": size,
        "location": location,
        "fov": fov,
        "heading": heading,
        "pitch": pitch,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.url
    else:
        print(f"Error: {response.status_code}")
        return None


def get_coordinates(api_key, address):
    
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return f"{latitude}, {longitude}"
    else:
        print(f"Error: {response.status_code}")
        print(data)
        return None



if __name__ == "__main__":
    
    address = input("Please input the address: ")
    location = get_coordinates(api_key, address)

    url = get_street_view_image(api_key, location, size="600x300", fov=90, heading=0, pitch=0)
    print(url)

