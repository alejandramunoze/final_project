
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, Blueprint, flash, redirect
from app.spreadsheet import fetch_spreadsheet
from app.street_view import get_street_view_image, get_coordinates

selection_routes = Blueprint('selection_routes', __name__)

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...
GOOGLE_MAPS_API = os.getenv("GOOGLE_MAPS_API")
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")


@selection_routes.route('/form')
def features():
    return render_template('selection_form.html')  

@selection_routes.route('/filter', methods=['POST'])
def filter_data():
    print(request.form)
    # Retrieve form data
    accomodation = request.form['type']
    single_num = request.form['single-num']
    double_num = request.form['double-num']
    bathroom_num = request.form['bathroom-num']

    # Get spreadsheet data
    df = fetch_spreadsheet(SPREADSHEET_URL)

    spreadsheet_data = df.to_dict("records")

    # Filter spreadsheet data based on selected data
    filtered_data = [entry for entry in spreadsheet_data if 
                     entry['type'] == accomodation and
                     entry['single-num'] == single_num and 
                     entry['double-num'] == double_num and
                     entry['bathroom-num'] == bathroom_num
                    ]

    # Extract addresses from filtered data
    addresses = [entry['address'] for entry in filtered_data]

    # Get coordinates for each address
    coordinates = [get_coordinates(GOOGLE_MAPS_API, address) for address in addresses]

    # Combine addresses, coordinates, and street view URLs into a list of dictionaries
    street_view_data = [
        {
            'address': address,
            'coordinates': coordinate,
            'street_view_url': get_street_view_image(GOOGLE_MAPS_API, coordinate)
        }
        for address, coordinate in zip(addresses, coordinates)
    ]

    if any(filtered_data):
    # Render a template to display filtered data
        return render_template('filtered_data.html', data=filtered_data, street_view_data=street_view_data)
    else:
        flash("No matches! Try again","danger")
        return redirect('/form')
        
