import sqlite3
from flask import jsonify, cursor
from flask import Flask, render_template, request
from flask import Flask
from flask_cors import CORS
from ..database.Tables import path_to_database
from datetime import datetime, timedelta
import random

bank_id = 400344

app = Flask(__name__)
CORS(app)

ShelfLife = 40 # A blood Unit is safe for 40 days
CurrentDate = "30-11-23" # Have a thread running which keeps updatig the current Date
CompatibilityProbability = 0.8

def execute_query(query):
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Welcome to the Blood Bank Management System!"

@app.route('/donor_registration', methods=['POST'])
def donor_registration():
    if request.method == 'POST':
        # Get form data
        data = request.json
        name = data['name']
        blood_group = data['bloodGroup']
        gender = data['gender']
        age = data['age']
        contact = data['contactNumber']
        date = data['donationDate']
        last_donated = date['lastDonated']
        admin_name = data['adminName']
        admin_password = data['adminPassword']

        conn = sqlite3.connect(path_to_database)
        cursor = conn.cursor()
        query = f"SELECT ADMIN_ID FROM REGISTERATION_TEAM WHERE ADMIN_NAME = {admin_name} AND ADMIN_PASSWORD = {admin_password}"
        cursor.execute(query)
        admin = cursor.fetchall()
        conn.close()

        insert_query = f"INSERT INTO DONOR (BANK_ID, ADMIN_ID, NAME, GENDER, AGE, BLOOD_GROUP,CONTACT, DONATION_DATE, LAST_DONATED) VALUES ({bank_id}, {admin}, {name}, {gender}, {age}, {blood_group}, {contact}, {date}, {last_donated})"
        execute_query(insert_query)

        print(f"Name: {name}, Blood Group: {blood_group}, Gender: {gender}, Contact: {contact}, Date: {date}")

        # You can now interact with the database and store the patient registration data

        return "Donor Registered Successfully!"

    return render_template('donor_registration.html')


@app.route('/patient_registration', methods=['POST'])
def patient_registration():
    if request.method == 'POST':
        # Get form data
        data = request.json
        name = data['name']
        blood_group = data['bloodGroup']
        gender = data['gender']
        contact = data['contact']
        date = data['date']
        admin_name = data['adminName']
        admin_password = data['adminPassword']

        conn = sqlite3.connect(path_to_database)
        cursor = conn.cursor()
        query = f"SELECT ADMIN_ID FROM REGISTERATION_TEAM WHERE ADMIN_NAME = {admin_name} AND ADMIN_PASSWORD = {admin_password}"
        cursor.execute(query)
        admin = cursor.fetchall()
        conn.close()

        insert_query = f"INSERT INTO PATIENT (ADMIN_ID, NAME, BLOOD_GROUP, GENDER, CONTACT, DATE) VALUES ({admin}, {name}, {blood_group}, {gender}, {contact}, {date})"
        execute_query(insert_query)

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
    # Process the data and add the new blood unit to the database
    # Make sure you have the necessary functions for database interaction
    # Return a response (e.g., success message or error)
    data = request.json
    donor_id = data['DonorID']
    analyst_id = data['AnalystID']
    number_of_units = data['NumberOfUnits']
    status = data['status']

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    for i in range(number_of_units):
        update_query = f"INSERT INTO BLOOD_UNIT (DONOR_ID, ANALYST_ID, STATUS) VALUES ({donor_id}, {analyst_id}, {status})"
        cursor.execute(update_query)
    conn.commit()
    conn.close()

    return jsonify({'message': 'Blood unit added successfully'})

@app.route('/update_blood_unit_status', methods=['POST'])
def update_blood_unit_status():
    data = request.json
    blood_unit_id = data['blood_unit_id']
    new_status = data['new_status']

    # Add code to update the status in the database
    update_query = f"UPDATE Blood_Unit SET Status = {new_status} WHERE Blood_Unit_ID = {blood_unit_id}"
    execute_query(update_query)

    return jsonify({'message': 'Blood unit status updated successfully'})

def is_compatible():
    result = random.random() < CompatibilityProbability
    if result:
        return True
    return False

def provide_the_blood_units(patient_id, compatible_units):
    print(f"These Units are compatible with the patient {compatible_units} and will be provided")
    blood_units = []

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    for units in compatible_units:
        blood_units.append(compatible_units[0])
        add_query = f"INSERT INTO Cross_Matching (Donor_ID, Patient_ID) VALUES ({compatible_units[1]}, {patient_id})"
        cursor.execute(add_query)

    update_query = f"UPDATE Blood_Unit SET Status = USED WHERE Blood_Unit_ID IN ({','.join(['?']*len(blood_units))})"
    cursor.execute(update_query)
    conn.commit()
    conn.close()

def make_blood_req(patient_id, blood_grp, quantity):
    # Query to get compatible blood units sorted by donation date
    non_expired_units = []
    non_expired_compatible_units = []
    query = f"""
        SELECT bu.Blood_Unit_ID, bu.Donor_ID, bu.Analyst_ID, bu.Status, d.Donation_Date
        FROM Blood_Unit bu
        JOIN Donor d ON bu.Donor_ID = d.Donor_ID
        WHERE d.Blood_Group = {blood_grp} AND bu.Status = 'InStock'
        ORDER BY d.Donation_Date;
    """
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    cursor.execute(query)
    compatible_units = cursor.fetchall()
    conn.commit()
    conn.close()

    # Check for expired units and update their status
    '''for unit in compatible_units:
        donation_date = datetime.strptime(unit['Donation_Date'], '%Y-%m-%d').date()
        expiration_date = donation_date + timedelta(days=40)
        if CurrentDate <= expiration_date:
            non_expired_units.append(unit)
        else:
            update_blood_unit_status(unit['Blood_Unit_ID'], 'Expired')'''
    
    non_expired_units = compatible_units
    print("THE NON Expired UNITS are =",non_expired_units)

    if len(non_expired_units) < quantity:
        print("Not enough blood, Cant supply as of now")
        return 0
    
    units = 0
    while(units < len(non_expired_units)):
        if quantity == 0:
            print("ALL the blood units are taken to be Given to the patient")
            provide_the_blood_units(patient_id, non_expired_compatible_units) # add all entries in cross matching and update all these Blood units as USED
            return len(non_expired_compatible_units)

        units = units + 1
        if is_compatible() == False:
            continue
        else:
            non_expired_compatible_units.append(non_expired_units[units])
            quantity = quantity - 1

    print("Not enough Blood Units Compatible with the Patient")
    return 0



@app.route('/make_blood_request', methods=['POST'])
def make_blood_request():
    data = request.json  # Assuming data is sent as JSON
    patient_id = data['patient_id']
    blood_grp = data['blood_grp']
    quantity = data['quantity']

    # Get the list of compatible blood units and make the request
    num_units_requested = make_blood_req(patient_id, blood_grp, quantity)

    return jsonify({'message': f'Successfully requested {num_units_requested} units of blood.'})

@app.route('/add_admin', methods=['POST'])
def add_admin():
    data = request.json
    admin_name = data['Username']
    admin_password = data['Password']

    # Execute a query to insert the admin
    query = f"INSERT INTO REGISTERATION_TEAM (username, password) VALUES ({admin_name}, {admin_password})"
    execute_query(query)

    return jsonify({'message': f'Successfully Added {admin_name}'})

@app.route('/remove_admin', methods=['POST'])
def remove_admin():
    data = request.json
    admin_id = data['id']

    query = f"DELETE FROM Registeration_Team WHERE Admin_ID = {admin_id}"
    execute_query(query)
    return jsonify({'message': f'Successfully Removed {admin_id}'})

@app.route('/update_admin', methods=['POST'])
def update_admin():
    data = request.json
    admin_id = data['id']
    new_admin_password = data['Password']

    query = f"UPDATE Registeration_Team SET Admin_Password = {new_admin_password} WHERE Admin_ID = {admin_id}"
    execute_query(query)
    return jsonify({"message': f'Successfully Updated {admin_id}'s Password"})

@app.route('/list_admin', methods=['POST'])
def list_admin():
    admin_list = []
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to insert the admin
    cursor.execute(f"SELECT * FROM REGISTERATION_TEAM")
    admins = cursor.fetchall()
    for i in admins:
        admin_list.append({f"ADMIN_ID = {i[0]}, ADMIN_NAME = {i[1]}, ADMIN_PASSWORD = {i[2]}"})

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return jsonify({"'admins': admins_list"})

@app.route('/add_analyst', methods=['POST'])
def add_analyst():
    data = request.json
    analyst_name = data['Username']
    analyst_password = data['Password']

    # Execute a query to insert the analyst
    query = f"INSERT INTO ANALYST (username, password) VALUES ({analyst_name}, {analyst_password})"
    execute_query(query)

    return jsonify({'message': f'Successfully Added {analyst_name}'})

@app.route('/remove_analyst', methods=['POST'])
def remove_analyst():
    data = request.json
    analyst_id = data['id']

    query = f"DELETE FROM ANALYST WHERE Analyst_ID = {analyst_id}"
    execute_query(query)
    return jsonify({'message': f'Successfully Removed {analyst_id}'})

@app.route('/update_analyst', methods=['POST'])
def update_analyst():
    data = request.json
    analyst_id = data['id']
    new_analyst_password = data['Password']

    query = f"UPDATE ANALYST SET Analyst_Password = {new_analyst_password} WHERE Analyst_ID = {analyst_id}"
    execute_query(query)
    return jsonify({"message': f'Successfully Updated {analyst_id}'s Password"})

@app.route('/list_analyst', methods=['POST'])
def list_analyst():
    analyst_list = []
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to insert the analyst
    cursor.execute(f"SELECT * FROM ANALYST")
    analysts = cursor.fetchall()
    for i in analysts:
        analyst_list.append({f"Analyst_ID = {i[0]}, Analyst_NAME = {i[1]}, Analyst_PASSWORD = {i[2]}"})

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return jsonify({"'analysts': analysts_list"})

@app.route('/donors_to_analyse', methods=['GET'])
def list_analyst():
    analyst_list = []
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to insert the analyst
    cursor.execute(f"SELECT * FROM ANALYST")
    analysts = cursor.fetchall()
    for i in analysts:
        analyst_list.append({f"Analyst_ID = {i[0]}, Analyst_NAME = {i[1]}, Analyst_PASSWORD = {i[2]}"})

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return jsonify({"'analysts': analysts_list"})


if __name__ == '__main__':
    app.run(debug=True, port = 5003)