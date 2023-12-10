from flask import Flask, render_template, request

app = Flask(__name__)

# Your spreadsheet data (replace this with your actual data)
spreadsheet_data = [
    {'neighbourhood': 'west-georgetown', 'type': 'house', 'room_num': '1', 'double_rooms': '1', 'bathroom_num': '2', 'patio': 'Y', 'parking': 'Y'},
    {'neighbourhood': 'burleith', 'type': 'apt', 'room_num': '2', 'double_rooms': '2', 'bathroom_num': '2', 'patio': 'N', 'parking': 'N'},
    # Other data entries...
]

@selection_routes.route('/')
def features():
    return render_template('selection_form.html')  

@selection_routes.route('/filter', methods=['POST'])
def filter_data():
    # Retrieve form data
    neighbourhood = request.form['neighbourhood']
    accomodation = request.form['type']
    single_num = request.form'single_num]
    
    # Filter spreadsheet data based on selected data
    filtered_data = [entry for entry in spreadsheet_data if 
                     entry['neighbourhood'] == neighbourhood and
                     entry['type'] == accomodation and
                     entry['single_num'] == single_num  
                     ]
    
    # Render a template to display filtered data
    return render_template('filtered_data.html', data=filtered_data, selected_neighbourhood=neighbourhood)
