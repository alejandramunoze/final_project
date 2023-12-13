
# street_view.py

import requests

def get_street_view_image(api_key, location, size="600x300", fov=90, heading=0, pitch=0):
    base_url = "https://maps.googleapis.com/maps/api/streetview"
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
