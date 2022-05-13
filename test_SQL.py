import sqlite3
import contactOrganizer

#create list of contacts
#will hard code this

contact1 = """Contact 1:
Erik Zale
345 College St
Hyattsville
MD
20494
311-573-4567
Argo37@gmail.com
"""

contact2 = """Contact 2:
Belle 
7001 Riverdale Ave
College Park
NY
30994
303-333-3030
012Fontiere@yahoo.com
"""
contact3 = """Contact 3:
Hannah Rivka
4578 Waterloo Way
Austin
TX
32456
202-745-0037
Hannah45@gmail.com
"""
# Create contact objects
contactOBJ1 = contactOrganizer.Contact(contact1)
contactOBJ2 = contactOrganizer.Contact(contact2)
contactOBJ3 = contactOrganizer.Contact(contact3)

#create a storage List for these contacts
myList = contactOrganizer.MyContactList()

#append the contact objects to list
myList.contactList.append(contactOBJ1)
myList.contactList.append(contactOBJ2)
myList.contactList.append(contactOBJ3)



#define connection and cursor

connection = sqlite3.Connection('contacts_list.db')

cursor = connection.cursor()

#create contact table

command1 = """ CREATE TABLE IF NOT EXISTS
contacts(Name VARCHAR(50), Address VARCHAR(50), Email VARCHAR(50), Phonenum VARCHAR(50))"""

cursor.execute(command1)

#this loop will add the contacts to a sql database
for x in myList.contactList:
    cursor.execute("INSERT INTO contacts VALUES(?, ?, ?, ?)", (x.name, x.address, x.email, x.phoneNum))



cursor.execute("SELECT * FROM contacts")

results = cursor.fetchall()

#commit change to the DB Browswer
connection.commit()

print(results)
