
import re

"""Test parse methods"""

contacts = open("oneContact.txt", "r")
readFile = contacts.read()

def parseName(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)")
        match = pattern.search(singleContactLine)
        return match.group(1).lstrip()

def parseEmail(singleContactLine):
        
        pattern = re.compile(r".+?@.+")
        match = pattern.search(singleContactLine)
        return match.group()
        
def parseAddress(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)")
        match = pattern.search(singleContactLine)

        street = match.group(2).lstrip()
        city = match.group(3).lstrip()
        state = match.group(4).lstrip()
        zipcode = match.group(5).lstrip()
        return street + ", " + city + ", " + state + ", " + zipcode

def parsePhoneNum(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)")
        match = pattern.search(singleContactLine)
        return match.group(6).lstrip()

print("Name: "+ str(parseName(readFile)))
print("Email: " + str(parseEmail(readFile)))
print("Address: " + str(parseAddress(readFile)))
print("Phone Number: " + str(parsePhoneNum(readFile)))
