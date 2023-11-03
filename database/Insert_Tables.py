import sqlite3

# Connect to the database
path_to_project = "/Users/amruth/BITS/Semister1/code/DBMS/blood-bank-management/"
path_to_database = path_to_project + "database/blood_bank_management.db"
conn = sqlite3.connect(path_to_database)
cursor = conn.cursor()

"""
INSERT INTO Manager (Manager_Name, Manager_Password)
VALUES ('manager', 'managerPassword');"""

query = """"""

cursor.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
