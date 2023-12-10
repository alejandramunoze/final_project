from flask import Flask, render_template, request, Blueprint
from app.spreadsheet import fetch_spreadsheet

selection_routes = Blueprint('selection_routes', __name__)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-NdNLEbaHBToP3eG_dBDNKhYcFeRkDTlwn0-_dK10Zs/edit?usp=sharing'
# Your spreadsheet data (replace this with your actual data)

spreadsheet_data = fetch_spreadsheet(spreadsheet_url)

@selection_routes.route('/form')
def features():
    return render_template('selection_form.html')  

@selection_routes.route('/filter', methods=['POST'])
def filter_data():
    # Retrieve form data
    neighbourhood = request.form['neighbourhood']
    accomodation = request.form['type']
    single_num = request.form['single_num']
    
    # Filter spreadsheet data based on selected data
    filtered_data = [entry for entry in spreadsheet_data if 
                     entry['neighbourhood'] == neighbourhood and
                     entry['type'] == accomodation and
                     entry['single_num'] == single_num  
                     ]
    
    # Render a template to display filtered data
    return render_template('filtered_data.html', data=filtered_data)
