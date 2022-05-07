from multiprocessing import connection
import sqlite3

#define connection and cursor

connection = sqlite3.Connection('contacts_list.db')

cursor = connection.cursor()

#create contact table

command1 = """ CREATE TABLE IF NOT EXISTS
contacts(name VARCHAR(50), Address VARCHAR(50), email VARCHAR(50), phonenum VARCHAR(50))"""

cursor.execute(command1)

cursor.execute("INSERT INTO contacts VALUES('Erik Zale', '345 College St, Hyattsville, MD, 20494', 'Argo37@gmail.com', '311-573-4567')")

cursor.execute("SELECT * FROM contacts")

results = cursor.fetchone()

print(results)
