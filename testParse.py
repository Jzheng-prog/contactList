
import re


contact1 = """
Contact 1:
Erik Zale
345 College St
Hyattsville
MD
20494
311-573-4567
Argo37@gmail.com
"""

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

print("Name: "+ str(parseName(contact1)))
print("Email: " + str(parseEmail(contact1)))
print("Address: " + str(parseAddress(contact1)))
print("Phone Number: " + str(parsePhoneNum(contact1)))
