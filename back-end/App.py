import sqlite3
from flask import jsonify, cursor
from flask import Flask, render_template, request
from flask import Flask
from flask_cors import CORS
from ..database.Tables import path_to_database
from datetime import datetime, timedelta
import random

app = Flask(__name__)
CORS(app)

ShelfLife = 40 # A blood Unit is safe for 40 days
CurrentDate = "30-11-23" # Have a thread running which keeps updatig the current Date
CompatibilityProbability = 0.8

@app.route('/')
def home():
    return "Welcome to the Blood Bank Management System!"

@app.route('/donor_registration', methods=['POST'])
def donor_registration():
    if request.method == 'POST':
        # Get form data
        data = request.get_json()
        name = data.get('name')
        gender = data.get('gender')
        age = data.get('age')
        blood_group = data.get('blood_group')
        contact = data.get('contact')
        donation_date = data.get('donation_date')
        last_donated = data.get('last_donated')

        # Process the data (e.g., interact with the database)
        # For now, let's print the data
        print(f"Name: {name}, Gender: {gender}, Age: {age}, Blood Group: {blood_group}, Contact: {contact}, Donation Date: {donation_date}, Last Donated: {last_donated}")

        # You can now interact with the database and store the data

        return "Donor Registered Successfully!"

    return render_template('donor_registration.html')


@app.route('/patient_registration', methods=['POST'])
def patient_registration():
    if request.method == 'POST':
        # Get form data
        data = request.get_json()
        name = data.get('name')
        blood_group = data.get('blood_groupme')
        gender = data.get('gender')
        contact = data.get('contact')
        date = data.get('date')

        # Process the data (e.g., interact with the database)
        # For now, let's print the data
        print(f"Name: {name}, Blood Group: {blood_group}, Gender: {gender}, Contact: {contact}, Date: {date}")

        # You can now interact with the database and store the patient registration data

        return "Patient Registered Successfully!"

    return render_template('patient_registration.html')

@app.route('/get_available_blood_units', methods=['GET'])
def get_available_blood_units():
    # Connect to the database
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to get available blood units
    cursor.execute("SELECT * FROM Blood_Unit WHERE Status = 'In Stock'")
    blood_units = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert results to a list of dictionaries for JSON response
    blood_units_list = [{'Blood_Unit_ID': unit[0], 'Donor_ID': unit[1], 'Analyst_ID': unit[2], 'Status': unit[3]} for unit in blood_units]

    return jsonify({'blood_units': blood_units_list})

@app.route('/add_blood_unit', methods=['POST'])
def add_blood_unit():
    data = request.json
    # Process the data and add the new blood unit to the database
    # Make sure you have the necessary functions for database interaction
    # Return a response (e.g., success message or error)
    return jsonify({'message': 'Blood unit added successfully'})

@app.route('/update_blood_unit_status', methods=['POST'])
def update_blood_unit_status():
    blood_unit_id = request.form['blood_unit_id']
    new_status = request.form['new_status']

    # Add code to update the status in the database
    # ...

    return jsonify({'message': 'Blood unit status updated successfully'})

def is_compatible():
    result = random.random() < CompatibilityProbability
    if result:
        return True
    return False


def make_blood_req(patient_id, blood_grp, quantity):
    # Query to get compatible blood units sorted by donation date
    non_expired_units = []
    non_expired_compatible_units = []
    query = """
        SELECT bu.Blood_Unit_ID, bu.Donor_ID, bu.Analyst_ID, bu.Status, d.Donation_Date
        FROM Blood_Unit bu
        JOIN Donor d ON bu.Donor_ID = d.Donor_ID
        WHERE d.Blood_Group = ? AND bu.Status = 'InStock'
        ORDER BY d.Donation_Date;
    """
    cursor.execute(query, (blood_grp,))
    compatible_units = cursor.fetchall()

    # Check for expired units and update their status
    # Check for expired units and update their status
    for unit in compatible_units:
        donation_date = datetime.strptime(unit['Donation_Date'], '%Y-%m-%d').date()
        expiration_date = donation_date + timedelta(days=40)
        if CurrentDate <= expiration_date:
            non_expired_units.append(unit)
        else:
            update_blood_unit_status(unit['Blood_Unit_ID'], 'Expired')


    if len(non_expired_units) < quantity:
        return "Not enough blood, Cant supply as of now"
    
    units = 0
    while(units < len(non_expired_units)):
        if quantity == 0:
            print("ALL the blood units are taken to be Given to the patient")
            provide_the_blood_units(non_expired_compatible_units) # add all entries in cross matching and update all these Blood units as USED
            return non_expired_compatible_units

        if is_compatible() == False:
            units = units + 1
            continue
        else:
            non_expired_compatible_units.append(non_expired_units[units])
            quantity = quantity - 1

    return "Not enough Blood Units COmpatible with the Patient"



@app.route('/make_blood_request', methods=['POST'])
def make_blood_request():
    data = request.json  # Assuming data is sent as JSON
    patient_id = data['patient_id']
    blood_grp = data['blood_grp']
    quantity = data['quantity']

    # Get the list of compatible blood units and make the request
    num_units_requested = make_blood_req(patient_id, blood_grp, quantity)

    return jsonify({'message': f'Successfully requested {num_units_requested} units of blood.'})


if __name__ == '__main__':
    app.run(debug=True, port = 5003)