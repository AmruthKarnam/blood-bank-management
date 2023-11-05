import sqlite3

# Connect to the database
path_to_project = "/Users/amruth/BITS/Semister1/code/DBMS/blood-bank-management/"
path_to_database = path_to_project + "database/blood_bank_management.db"
conn = sqlite3.connect(path_to_database)
cursor = conn.cursor()

# Define SQL queries to create tables
queries = [
    """
    CREATE TABLE Manager (
        Manager_ID INTEGER PRIMARY KEY,
        Manager_Name TEXT NOT NULL,
        Manager_Password TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE Registration_team (
        Admin_ID INTEGER PRIMARY KEY,
        Admin_Name TEXT NOT NULL,
        Admin_Password TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE Analyst (
        Analyst_ID INTEGER PRIMARY KEY,
        Analyst_Name TEXT NOT NULL,
        Analyst_Password TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE Blood_Unit (
        Blood_Unit_ID INTEGER PRIMARY KEY,
        Donor_ID INTEGER NOT NULL,
        Analyst_ID INTEGER NOT NULL,
        Status TEXT CHECK(Status IN ('InStock', 'PendingAnalysis', 'Expired', 'Damaged', 'Used')),
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID),
        FOREIGN KEY (Analyst_ID) REFERENCES Analyst(Analyst_ID)
    );
    """,
    """
    CREATE TABLE Donor (
        Donor_ID INTEGER PRIMARY KEY,
        Bank_ID INTEGER NOT NULL,
        Admin_ID INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Gender TEXT CHECK(Gender IN ('Male', 'Female')),
        Age INTEGER CHECK(Age >= 0),
        Blood_Group TEXT CHECK(Blood_Group IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
        Contact TEXT NOT NULL,
        Donation_Date DATE NOT NULL,
        Last_Donated DATE NOT NULL,
        FOREIGN KEY (Bank_ID) REFERENCES Blood_Bank(Bank_ID),
        FOREIGN KEY (Admin_ID) REFERENCES Registration_team(Admin_ID)
    );
    """,
    """
    CREATE TABLE Hospital (
        Hospital_ID INTEGER PRIMARY KEY,
        Requested_Bank_ID INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Address TEXT NOT NULL,
        City TEXT NOT NULL,
        Pincode INTEGER NOT NULL,
        FOREIGN KEY (Requested_Bank_ID) REFERENCES Blood_Bank(Bank_ID)
    );
    """,
    """
    CREATE TABLE Patient (
        Patient_ID INTEGER PRIMARY KEY,
        Admin_ID INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Blood_Group TEXT CHECK(Blood_Group IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
        Gender TEXT CHECK(Gender IN ('Male', 'Female')),
        Contact TEXT NOT NULL,
        Date DATE NOT NULL,
        FOREIGN KEY (Admin_ID) REFERENCES Registration_team(Admin_ID)
    );
    """,
    """
    CREATE TABLE Blood_Bank (
        Bank_ID INTEGER PRIMARY KEY,
        Affiliated_Hospital_ID INTEGER NOT NULL,
        Bank_Name TEXT NOT NULL,
        Manager_ID INTEGER NOT NULL,
        FOREIGN KEY (Affiliated_Hospital_ID) REFERENCES Hospital(Hospital_ID),
        FOREIGN KEY (Manager_ID) REFERENCES Manager(Manager_ID)
    );
    """,
    """
    CREATE TABLE Cross_Matching (
        Cross_Matching_ID INTEGER PRIMARY KEY,
        BloodUnit_ID INTEGER NOT NULL,
        Patient_ID INTEGER NOT NULL,
        Matching_Result TEXT CHECK(Matching_Result IN ('Positive', 'Negative')),
        Matching_Date DATE NOT NULL,
        FOREIGN KEY (BloodUnit_ID) REFERENCES Blood_Unit(Blood_Unit_ID),
        FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
    );
    """,
    """
    CREATE TABLE Diseases (
        Donor_ID INTEGER NOT NULL,
        Diseases TEXT NOT NULL,
        PRIMARY KEY (Donor_ID, Diseases),
        FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID)
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
