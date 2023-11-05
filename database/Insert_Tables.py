import sqlite3

# Connect to the database
path_to_project = "/Users/amruth/BITS/Semister1/code/DBMS/blood-bank-management/"
path_to_database = path_to_project + "database/blood_bank_management.db"
conn = sqlite3.connect(path_to_database)
cursor = conn.cursor()

"""
INSERT INTO Manager (Manager_ID, Manager_Name, Manager_Password) VALUES (1, 'Manager', 'ManagerPassword');
"""
"""
INSERT INTO Registration_team (Admin_ID, Admin_Name, Admin_Password) VALUES (1, 'Admin', 'AdminPassword');
"""
"""
INSERT INTO Analyst (Analyst_ID, Analyst_Name, Analyst_Password) VALUES (1, 'Analyst', 'AnalystPassword');
"""
"""
INSERT INTO Donor (Donor_ID, Bank_ID, Admin_ID, Name, Gender, Age, Blood_Group, Contact, Donation_Date, Last_Donated) VALUES (1, 1, 1, 'John Doe', 'Male', 30, 'A+', '1234567890', '2023-11-01', '2023-04-01');
INSERT INTO Donor (Donor_ID, Bank_ID, Admin_ID, Name, Gender, Age, Blood_Group, Contact, Donation_Date, Last_Donated) VALUES (2, 1, 1, 'Jane Doe', 'Female', 25, 'B+', '0987654321', '2023-11-01', '2023-04-01');
INSERT INTO Donor (Donor_ID, Bank_ID, Admin_ID, Name, Gender, Age, Blood_Group, Contact, Donation_Date, Last_Donated) VALUES (3, 1, 1, 'Jim Doe', 'Male', 35, 'AB+', '5555555555', '2023-11-01', '2023-04-01');
INSERT INTO Donor (Donor_ID, Bank_ID, Admin_ID, Name, Gender, Age, Blood_Group, Contact, Donation_Date, Last_Donated) VALUES (4, 1, 1, 'Jill Doe', 'Female', 40, 'O+', '6666666666', '2023-11-01', '2023-04-01');

"""
"""
INSERT INTO Diseases (Donor_ID, Diseases) VALUES 
  (2, 'Hepatitis B'),
  (4, 'HIV');
"""
"""
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (1, 1, 1, 'InStock');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (2, 2, 1, 'Damaged');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (3, 3, 1, 'InStock');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (4, 4, 1, 'Damaged');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (5, 1, 1, 'InStock');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (6, 1, 1, 'InStock');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (7, 1, 1, 'InStock');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (8, 2, 1, 'Damaged');
INSERT INTO Blood_Unit (Blood_Unit_ID, Donor_ID, Analyst_ID, Status) VALUES (9, 2, 1, 'Damaged');

"""

"""
INSERT INTO Hospital (Hospital_ID, Requested_Bank_ID, Name, Address, City, Pincode) VALUES (1, 1, 'Hospital A', '123 Street', 'City A', 123456);
INSERT INTO Hospital (Hospital_ID, Requested_Bank_ID, Name, Address, City, Pincode) VALUES (2, 1, 'Hospital B', '456 Street', 'City A', 654321);
INSERT INTO Hospital (Hospital_ID, Requested_Bank_ID, Name, Address, City, Pincode) VALUES (3, 1, 'Hospital C', '789 Street', 'City A', 987654);
"""

"""
INSERT INTO Patient (Patient_ID, Admin_ID, Name, Blood_Group, Gender, Contact, Date) VALUES (1, 1, 'Jane Doe', 'B+', 'Female', '0987654321', '2023-11-01');
INSERT INTO Patient (Patient_ID, Admin_ID, Name, Blood_Group, Gender, Contact, Date) VALUES (2, 1, 'John Smith', 'A+', 'Male', '5555555555', '2023-11-01');
"""

"""
INSERT INTO Blood_Bank (Bank_ID, Affiliated_Hospital_ID, Bank_Name, Manager_ID) VALUES (1, 1, 'Blood Bank A', 1);
"""

"""
INSERT INTO Cross_Matching (Cross_Matching_ID, BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES (1, 1, 1, 'Positive', '2023-11-01');
INSERT INTO Cross_Matching (Cross_Matching_ID, BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES (2, 3, 1, 'Positive', '2023-11-01');
INSERT INTO Cross_Matching (Cross_Matching_ID, BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES (3, 5, 1, 'Negative', '2023-11-01');
INSERT INTO Cross_Matching (Cross_Matching_ID, BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES (4, 6, 2, 'Positive', '2023-11-01');
INSERT INTO Cross_Matching (Cross_Matching_ID, BloodUnit_ID, Patient_ID, Matching_Result, Matching_Date) VALUES (5, 7, 2, 'Negative', '2023-11-01');

"""

query = "INSERT INTO Hospital (Hospital_ID, Requested_Bank_ID, Name, Address, City, Pincode) VALUES (3, 1, 'Hospital C', '789 Street', 'City A', 987654);"

cursor.execute(query)
conn.commit()


# Close the connection
conn.close()
