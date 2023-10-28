from flask import Flask, render_template, request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


if __name__ == '__main__':
    app.run(debug=True, port = 5003)