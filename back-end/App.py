import sqlite3
from flask import jsonify
from flask import Flask, render_template, request
from flask_cors import CORS
from datetime import datetime, timedelta
import random
from datetime import datetime, timedelta

bank_id = 1
path_to_project = "/Users/amruth/BITS/Semister1/code/DBMS/blood-bank-management/"
path_to_database = path_to_project + "database/blood_bank_management.db"

ShelfLife = 40 # A blood Unit is safe for 40 days
CurrentDate = "30-11-23" # Have a thread running which keeps updatig the current Date
CompatibilityProbability = 0.8

app = Flask(__name__)
CORS(app)

def execute_query(query):
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Welcome to the Blood Bank Management System!"

def check_if_donatable(date, last_donated):
    date = datetime.strptime(date, '%Y-%m-%d')
    last_donated = datetime.strptime(last_donated, '%Y-%m-%d')

    # Calculate the difference in days
    if date < last_donated:
        return -1

    difference = (date - last_donated).days
    # Check if the difference is at least 6 months (approximately 180 days)
    if difference >= 180:
        print("The difference is at least 6 months.")
        return 1
    else:
        print("The difference is less than 6 months.")
        return 0

@app.route('/donor_registration', methods=['POST'])
def donor_registration():
    if request.method == 'POST':
        # Get form data
        data = request.json
        name = data['name']
        gender = data['gender']
        age = data['age']
        blood_group = data['blood_group']
        contact_number = data['contactNumber']
        date = data['donationDate']
        last_donated = data['lastDonated']
        admin_name = data['adminName']
        admin_password = data['adminPassword']

        print(f"INSIDE admin name = BG= {blood_group} {admin_name} {contact_number} {age} {name} and {admin_password} {date} {last_donated}")
        state = check_if_donatable(date, last_donated)
        if state == 1:
            conn = sqlite3.connect(path_to_database)
            cursor = conn.cursor()
            query = f"SELECT ADMIN_ID FROM REGISTRATION_TEAM WHERE ADMIN_NAME = '{admin_name}' AND ADMIN_PASSWORD = '{admin_password}'"
            cursor.execute(query)
            admin = cursor.fetchone()
            conn.close()

            insert_query = f"INSERT INTO DONOR (BANK_ID, ADMIN_ID, Name, Gender, Age, Blood_Group, Contact, Donation_Date, Last_Donated) VALUES ({bank_id}, {admin[0]}, '{name}', '{gender}', {age}, '{blood_group}', '{contact_number}', '{date}', '{last_donated}')"
            print(insert_query)
            execute_query(insert_query)

            print(f"Name: {name}, Blood Group: {blood_group}, Gender: {gender}, Contact: {contact_number}, Date: {date}")

            # You can now interact with the database and store the patient registration data

            return jsonify({"message" : "Donor Registered Successfully!"})
        
        elif state == 0:
            return jsonify({"message" : "Can't Donate before 6 months of last donation"})
        
        else:
            return jsonify({"message" : "Last donated date is greater than current date"})

    return jsonify({"message" : "Couldnt register"})


@app.route('/patient_registration', methods=['POST'])
def patient_registration():
    if request.method == 'POST':
        # Get form data
        data = request.json
        name = data['name']
        blood_group = data['blood_group']
        gender = data['gender']
        contact = data['contact']
        date = data['date']
        admin_name = data['adminName']
        admin_password = data['adminPassword']
        print(f"Inside patient registeration {name} {blood_group} {gender} {contact} {date} {admin_name} {admin_password}")

        conn = sqlite3.connect(path_to_database)
        cursor = conn.cursor()
        query = f"SELECT Admin_ID FROM REGISTRATION_TEAM WHERE Admin_Name = '{admin_name}' AND Admin_Password = '{admin_password}'"
        cursor.execute(query)
        admin = cursor.fetchone()
        conn.close()

        insert_query = f"INSERT INTO PATIENT (ADMIN_ID, NAME, BLOOD_GROUP, GENDER, CONTACT, DATE) VALUES ({admin[0]}, '{name}', '{blood_group}', '{gender}', '{contact}', '{date}')"
        execute_query(insert_query)

        print(f"Name: {name}, Blood Group: {blood_group}, Gender: {gender}, Contact: {contact}, Date: {date}")

        # You can now interact with the database and store the patient registration data

        return jsonify({"message" : "Patient Registered Successfully!"})

    return jsonify({"message" : "Couldnt register"})

@app.route('/get_available_blood_units', methods=['GET'])
def get_available_blood_units():
    # Connect to the database
    print("inside get blood units")
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to get available blood units
    cursor.execute("SELECT * FROM Blood_Unit WHERE Status = 'InStock'")
    blood_units = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert results to a list of dictionaries for JSON response
    blood_units_list = [{'Blood_Unit_ID': unit[0], 'Status': unit[3]} for unit in blood_units]
    print(blood_units_list)

    return jsonify({'blood_units': blood_units_list})

@app.route('/add_blood_unit', methods=['POST'])
def add_blood_unit():
    # Process the data and add the new blood unit to the database
    # Make sure you have the necessary functions for database interaction
    # Return a response (e.g., success message or error)
    print(f"Inside add blood Units")
    data = request.json
    donor_id = data['DonorID']
    analyst_id = data['AnalystID']
    number_of_units = int(data['NumberOfUnits'])
    status = "PendingAnalysis"
    print(f"Inside add_blood_units {donor_id} {analyst_id} {number_of_units} {status}")

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    for i in range(number_of_units):
        update_query = f"INSERT INTO BLOOD_UNIT (DONOR_ID, ANALYST_ID, STATUS) VALUES ({donor_id}, {analyst_id}, '{status}')"
        cursor.execute(update_query)
    conn.commit()
    conn.close()

    return jsonify({'message': 'Blood unit added successfully'})

@app.route('/update_blood_unit_status', methods=['POST'])
def update_blood_unit_status():
    print(f"inside update")
    data = request.json
    blood_unit_id = request.form.get('blood_unit_id')
    new_status = request.form.get('new_status')
    print(f"inside update {blood_unit_id} {new_status}")

    # Add code to update the status in the database
    update_query = f"UPDATE Blood_Unit SET Status = '{new_status}' WHERE Blood_Unit_ID = {blood_unit_id}"
    execute_query(update_query)

    return jsonify({'message': 'Blood unit status updated successfully'})

def is_compatible():
    result = random.random() < CompatibilityProbability
    if result:
        return True
    return False

# Check for expired units and update their status
'''for unit in compatible_units:
    donation_date = datetime.strptime(unit['Donation_Date'], '%Y-%m-%d').date()
    expiration_date = donation_date + timedelta(days=40)
    if CurrentDate <= expiration_date:
        non_expired_units.append(unit)
    else:
        update_blood_unit_status(unit['Blood_Unit_ID'], 'Expired')'''


def make_blood_req(id, blood_grp, quantity, status, req_by):
    matching_date = CurrentDate
    non_expired_compatible_units = []
    add_query = []
    query = f"""
        SELECT bu.Blood_Unit_ID, bu.Donor_ID, bu.Analyst_ID, bu.Status, d.Donation_Date
        FROM Blood_Unit bu
        JOIN Donor d ON bu.Donor_ID = d.Donor_ID
        WHERE d.Blood_Group = '{blood_grp}' AND bu.Status = 'InStock'
        ORDER BY d.Donation_Date;
    """
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    cursor.execute(query)
    compatible_units = cursor.fetchall()
    conn.commit()
    conn.close()

    non_expired_units = compatible_units
    print("THE NON Expired UNITS are =",non_expired_units)

    if len(compatible_units) < quantity:
        return "Not enough blood, Can't supply as of now"
    
    if req_by == "HOSPITAL":
        # Use parameterized query and execute many
        update_query = f"UPDATE Blood_Unit SET Status = '{status}' WHERE Blood_Unit_ID = ({','.join(['?']*len(non_expired_units))})"
        print("QUERY HOSPITAL is =", update_query)
        execute_query(update_query)
        return f"Successfully Reserved {len(compatible_units)} units For Hospital {id}"
    
    else:
        units = 0
        while(units < len(compatible_units)):
            if quantity == 0:
                # Use parameterized query and execute
                conn = sqlite3.connect(path_to_database)
                cursor = conn.cursor()
                update_query = f"""
                    UPDATE Blood_Unit
                    SET Status = '{status}'
                    WHERE Blood_Unit_ID IN ({','.join(str(blood_unit[0]) for blood_unit in non_expired_compatible_units)});
                """
                cursor.execute(update_query)
                for query in add_query:
                    cursor.execute(add_query)
                conn.commit()
                conn.close()
                return f"Successfully supplied {len(non_expired_compatible_units)} units of blood"

            if is_compatible() == False:
                matching_result = "Negative"
            else:
                matching_result = "Positive"
                non_expired_compatible_units.append(non_expired_units[units])
                quantity -= 1

            add_query.append(f"INSERT INTO Cross_Matching (BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES ({non_expired_units[0][0]}, {id}, '{matching_result}', '{matching_date}')")
            units += 1

        conn = sqlite3.connect(path_to_database)
        cursor = conn.cursor()
        for query in add_query:
            cursor.execute(add_query)
        conn.commit()
        conn.close()
        return "Not enough Blood Units Compatible with the Patient"

@app.route('/make_blood_request', methods=['POST'])
def make_blood_request():
    data = request.json  # Assuming data is sent as JSON
    patient_id = data['patientID']
    blood_grp = data['bloodGroup']
    quantity = int(data['quantity'])
    print(f"Make blood req {patient_id} {blood_grp} {quantity}")

    # Get the list of compatible blood units and make the request
    num_units_requested = make_blood_req(patient_id, blood_grp, quantity, "USED", "PATIENT")

    return jsonify({'message': f'{num_units_requested}'})

@app.route('/add_admin', methods=['POST'])
def add_admin():
    data = request.json
    admin_name = data['username']
    admin_password = data['password']
    print(f"Inside add_admin {admin_name} {admin_password}")

    # Execute a query to insert the admin
    query = f"INSERT INTO REGISTRATION_TEAM (Admin_Name, Admin_Password) VALUES ('{admin_name}', '{admin_password}')"
    execute_query(query)

    return jsonify({'message': f'Successfully Added {admin_name}'})

@app.route('/remove_admin', methods=['DELETE'])
def remove_admin():
    data = request.json
    admin_id = data['username']
    print(f"Inside remove_admin {admin_id}")

    query = f"DELETE FROM REGISTRATION_TEAM WHERE Admin_ID = {admin_id}"
    execute_query(query)
    return jsonify({'message': f'Successfully Removed {admin_id}'})

@app.route('/update_admin', methods=['PUT'])
def update_admin():
    data = request.json
    admin_id = data['username']
    new_admin_password = data['newPassword']
    print(f"Inside update_admin {admin_id} {new_admin_password}")

    query = f"UPDATE REGISTRATION_TEAM SET Admin_Password = '{new_admin_password}' WHERE Admin_ID = {admin_id}"
    execute_query(query)
    return jsonify({"message": f"Successfully Updated {admin_id}'s Password"})

@app.route('/list_admins', methods=['GET'])
def list_admin():
    admin_list = []
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()
    print(f"Inside list_admin")

    # Execute a query to insert the admin
    cursor.execute(f"SELECT * FROM REGISTRATION_TEAM")
    admins = cursor.fetchall()
    for i in admins:
        admin_list.append({f"ADMIN_ID" : i[0], "ADMIN_NAME" : i[1], "ADMIN_PASSWORD" : i[2]})

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(admin_list)
    return jsonify({"admins": admin_list})

@app.route('/add_analyst', methods=['POST'])
def add_analyst():
    data = request.json
    analyst_name = data['username']
    analyst_password = data['password']
    print("Inside add_analyst {analyst_name} {analyst_password}")

    # Execute a query to insert the analyst
    query = f"INSERT INTO ANALYST (Analyst_Name, Analyst_Password) VALUES ('{analyst_name}', '{analyst_password}')"
    print(query)
    execute_query(query)

    return jsonify({'message': f'Successfully Added {analyst_name}'})

@app.route('/remove_analyst', methods=['DELETE'])
def remove_analyst():
    print(f"inside remove analyst")
    data = request.json
    analyst_id = data['username']

    print(f"inside remove_analyst {analyst_id}")
    query = f"DELETE FROM ANALYST WHERE Analyst_ID = {analyst_id}"
    execute_query(query)
    return jsonify({'message': f'Successfully Removed {analyst_id}'})

@app.route('/update_analyst', methods=['PUT'])
def update_analyst():
    print(f"inside update_analyst")
    data = request.json
    analyst_id = data['username']
    new_analyst_password = data['newPassword']
    print(f"Inside update_analyst {analyst_id} {new_analyst_password}")

    query = f"UPDATE ANALYST SET Analyst_Password = '{new_analyst_password}' WHERE Analyst_ID = {analyst_id}"
    execute_query(query)
    return jsonify({"message": f"Successfully Updated {analyst_id}'s Password"})

@app.route('/list_analyst', methods=['GET'])
def list_analyst():
    print(f"Inside list_analyst")
    analyst_list = []
    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to insert the analyst
    cursor.execute(f"SELECT * FROM ANALYST")
    analysts = cursor.fetchall()
    for i in analysts:
        analyst_list.append({f"Analyst_ID" : i[0], "Analyst_NAME" : i[1], "Analyst_PASSWORD" : i[2]})

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(analyst_list)
    return jsonify({"analyst": analyst_list})

@app.route('/donors_to_analyse', methods=['GET'])
def donors_to_analyse():
    print(f"HELLLOO INSIDE DONORS TO ANALYSE\n")
    analyst_name = request.args.get('analystName')
    analyst_password = request.args.get('analystPassword')

    print(f"inside donors_to_analyse {analyst_name} {analyst_password}")

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to get the analyst with the provided credentials
    cursor.execute(f"SELECT * FROM Analyst WHERE Analyst_Name = '{analyst_name}' AND Analyst_Password = '{analyst_password}'")
    analyst_id = cursor.fetchone()

    if analyst_id is None:
        return jsonify({'message': 'Analyst not found'})

    cursor.execute(f"SELECT bu.Donor_ID FROM Blood_Unit bu WHERE bu.Analyst_ID = {analyst_id[0]} AND bu.Status ='PendingAnalysis' ")
    donors_to_analyse = cursor.fetchall()
    print(f"\n{donors_to_analyse}\n")
    donors = set(donors_to_analyse)
    print(f"\n{donors}\n")

    # Close the connection
    conn.close()
    print(f" Name is {analyst_name} and Password is {analyst_password}\n")
    print(f"analyst= {analyst_id}")

    donors_list = [{'Donor_ID': donor[0]} for donor in donors]
    print(donors_list)

    return jsonify({'donors': donors_list})


@app.route('/list_donor_diseases', methods=['POST'])
def list_donor_analysis():
    data = request.json
    donor_id = data['donor_id']

    print(f"The donor is {donor_id}")

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    # Execute a query to get the diseases for the specified donor
    cursor.execute(f"SELECT Diseases FROM Diseases WHERE Donor_ID = {donor_id}")
    diseases = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert results to a list of diseases
    diseases_list = [row[0] for row in diseases]

    return jsonify({'diseases': diseases_list})

@app.route('/add_donor_analysis', methods=['POST'])
def add_donor_analysis():
    data = request.json
    donor_id = data['donorId']
    diseases = data['diseases']  # Assuming diseases is a list of selected diseases

    print(f"{donor_id} and {diseases}")

    conn = sqlite3.connect(path_to_database)
    cursor = conn.cursor()

    try:
        # Begin a transaction
        conn.execute('BEGIN TRANSACTION')

        # Insert diseases into Diseases table
        for disease in diseases:
            cursor.execute(f"INSERT INTO Diseases (Donor_ID, Diseases) VALUES ({donor_id}, '{disease}')")

        # Update status of blood units associated with this donor
        if len(diseases) > 0:
            cursor.execute(f"UPDATE Blood_Unit SET Status = 'Damaged' WHERE Donor_ID = {donor_id}")
        else:
            cursor.execute(f"UPDATE Blood_Unit SET Status = 'InStock' WHERE Donor_ID = {donor_id}")

        # Commit the transaction
        conn.execute('COMMIT')
        return jsonify({'message': 'Donor analysis added successfully'})
    except Exception as e:
        # If an error occurs, rollback the transaction
        conn.execute('ROLLBACK')
        return jsonify({'message': f'Error: {str(e)}'}), 500
    finally:
        # Close the connection
        conn.close()
    
@app.route('/hospital_request', methods=['POST'])
def hospital_request():
    hospital_id = request.form.get('hospital_id')
    blood_group = request.form.get('blood_group')
    quantity = request.form.get('quantity')

    print(f"Make blood req {hospital_id} {blood_group} {quantity}")

    # Get the list of compatible blood units and make the request
    num_units_requested = make_blood_req(hospital_id, blood_group, quantity, "RESERVED", "HOSPITAL")

    return jsonify({'message': f'{num_units_requested}'})


if __name__ == '__main__':
    app.run(debug=True, port = 5000)