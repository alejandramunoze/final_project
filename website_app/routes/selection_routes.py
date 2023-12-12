from flask import Flask, render_template, request, Blueprint, flash, redirect
from app.spreadsheet import fetch_spreadsheet

selection_routes = Blueprint('selection_routes', __name__)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-NdNLEbaHBToP3eG_dBDNKhYcFeRkDTlwn0-_dK10Zs/edit?usp=sharing'




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
    df = fetch_spreadsheet(spreadsheet_url)

    spreadsheet_data = df.to_dict("records")

    # Filter spreadsheet data based on selected data
    filtered_data = [entry for entry in spreadsheet_data if 
                     entry['type'] == accomodation and
                     entry['single-num'] == single_num and 
                     entry['double-num'] == double_num and
                     entry['bathroom-num'] == bathroom_num
                    ]

    if any(filtered_data):
    # Render a template to display filtered data
        return render_template('filtered_data.html', data=filtered_data)
    else:
        flash("No matches! Try again","danger")
        return redirect('/form')
        
