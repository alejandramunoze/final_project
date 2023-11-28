



import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, Blueprint
from app.street_view import get_street_view_image


load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

GOOGLE_MAPS_API = os.getenv("GOOGLE_MAPS_API")


house_routes = Blueprint('house_routes', __name__)

@house_routes.route('/house')
def house():

    api_key = GOOGLE_MAPS_API
    # Replace 'LATITUDE,LONGITUDE' with the actual coordinates (e.g., '40.748817,-73.985428')
    location = '40.748817,-73.985428'

    image_url = get_street_view_image(api_key, location)

    # Render the HTML template with the image URL
    return render_template('house.html', image_url=image_url)

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(house_routes)

if __name__ == '__main__':
    app.run(debug=True)
