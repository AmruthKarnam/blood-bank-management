import sqlite3

# Connect to the database
path_to_project = "/Users/amruth/BITS/Semister1/code/DBMS/blood-bank-management/"
path_to_database = path_to_project + "database/blood_bank_management.db"
conn = sqlite3.connect(path_to_database)
cursor = conn.cursor()

# Define SQL queries to create tables
queries = [
    """
    CREATE TABLE Cross_Matching (
        Cross_Matching_ID INTEGER PRIMARY KEY,
        Blood_Unit_ID INTEGER,
        Patient_ID INTEGER,
        Matching_Result TEXT,
        Matching_Date DATE,
        FOREIGN KEY (Blood_Unit_ID) REFERENCES Blood_Unit(Blood_Unit_ID),
        FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
    );
    """,
    """
    CREATE TABLE Blood_Unit (
        Blood_Unit_ID INTEGER PRIMARY KEY,
        Donor_ID INTEGER,
        Analyst_ID INTEGER,
        Status TEXT,
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID),
        FOREIGN KEY (Analyst_ID) REFERENCES Analyst(Analyst_ID)
    );
    """,
    """
    CREATE TABLE Diseases (
        Donor_ID INTEGER,
        Disease TEXT,
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID)
    );
    """,
    """
    CREATE TABLE Donor (
        Donor_ID INTEGER PRIMARY KEY,
        Bank_ID INTEGER,
        Admin_ID INTEGER,
        Name TEXT,
        Gender TEXT,
        Age INTEGER,
        Blood_Group TEXT,
        Contact TEXT,
        Donation_Date DATE,
        Last_Donated DATE,
        FOREIGN KEY (Bank_ID) REFERENCES Blood_Bank(Bank_ID),
        FOREIGN KEY (Admin_ID) REFERENCES Registration_team(Admin_ID)
    );
    """,
    """
    CREATE TABLE Patient (
        Patient_ID INTEGER PRIMARY KEY,
        Admin_ID INTEGER,
        Name TEXT,
        Blood_Grp TEXT,
        Gender TEXT,
        Contact TEXT,
        Date DATE,
        FOREIGN KEY (Admin_ID) REFERENCES Registration_team(Admin_ID)
    );
    """,
    """
    CREATE TABLE Hospital (
        Hospital_ID INTEGER PRIMARY KEY,
        Requested_Bank_ID INTEGER,
        Name TEXT,
        Address TEXT,
        City TEXT,
        Pincode TEXT,
        FOREIGN KEY (Requested_Bank_ID) REFERENCES Blood_Bank(Bank_ID)
    );
    """,
    """
    CREATE TABLE Blood_Bank (
        Bank_ID INTEGER PRIMARY KEY,
        Affiliated_Hospital_ID INTEGER,
        Bank_Name TEXT,
        Manager_ID INTEGER,
        FOREIGN KEY (Affiliated_Hospital_ID) REFERENCES Hospital(Hospital_ID),
        FOREIGN KEY (Manager_ID) REFERENCES Manager(Manager_ID)
    );
    """,
    """
   CREATE TABLE Manager (
        Manager_ID INTEGER PRIMARY KEY,
        Manager_Name TEXT,
        Manager_Password TEXT
    );

    """,
    """
    CREATE TABLE Registration_team (
        Admin_ID INTEGER PRIMARY KEY,
        Admin_Name TEXT,
        Admin_Password TEXT
    );

    """,
    """
   CREATE TABLE Analyst (
        Analyst_ID INTEGER PRIMARY KEY,
        Analyst_Name TEXT,
        Analyst_Password TEXT
    );
    """
]

# Execute the SQL queries
for query in queries:
    cursor.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
