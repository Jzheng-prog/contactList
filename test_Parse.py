
import re

from contactOrganizer import parseName, parseEmail, parseAddress, parsePhoneNum

"""Test parse methods"""

contacts = open("oneContact.txt", "r")
readFile = contacts.read()

def test_parseName():
        name = parseName(readFile)

        assert name == "Erik Zale", "Not the right name."

def test_parseEmail():
        
        email = parseEmail(readFile)
        
        assert email == "Argo37@gmail.com", "Not the right email."
        
def test_parseAddress():
        
        address = parseAddress(readFile)

        assert address == "345 College St, Hyattsville, MD, 20494", "Not the right address."

def test_parsePhoneNum():

        phoneNum = parsePhoneNum(readFile)

        assert phoneNum == "311-573-4567", "Not the right phoneNum."

       

print("Name: "+ str(parseName(readFile)))
print("Email: " + str(parseEmail(readFile)))
print("Address: " + str(parseAddress(readFile)))
print("Phone Number: " + str(parsePhoneNum(readFile)))
