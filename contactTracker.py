
import re
import sys
import argparse

"""We will have a list of contacts, with the names, emails, phone number, and addresses. This could be one or more. We will parse
through the list, break them up into individual objects, and then we can have different methods/functions
to organized them base on the broken parts, for example
we can break organized them by name (alphabetacle order) or by phone number."""


"""One contact object contains names, emails, phone number, and addresses. There will be a list of contact objects in another class 
called MyContactList."""
class Contact:

    def __init__(self, singleContactLine):

        self.name = parseName(singleContactLine)
        self.email = parseEmail(singleContactLine)
        self.address = parseAddress(singleContactLine)
        self.PhoneNum = parsePhoneNum(singleContactLine)

"""Functions below helps us parse throught he context to fine the information we want"""

"""Bushrah"""
def parseContact(singleContactLine):
        pass
"""Bushrah"""
def parseName(singleContactLine):
        pass

"""John"""
"""pasrseEmail does not inlcude all scenerios."""
def parseEmail(singleContactLine):

        pattern = re.compile(r"\w+@\w+.+")
        match = pattern.search(singleContactLine)
        return match

"""Derek"""
def parseAddress(singleContactLine):
        pass
"""Derek"""
def parsePhoneNum(singleContactLine):
        pass




"""MyContackList class will have a list of contact objects, and can manipulate/sort contact Objects"""
class MyContactList:
        def __init__(self):
                self.contactList = []

        """Add the contact object to a list of contacts""""""John"""
        def addContactToList(self, Contact):
                self.contactList.append(Contact)

        """"Sort the list""""""John"""
        def sortList():
                pass

"""Main would not work right now, cause each line is not a new contact, rather part of a contact. Need revision."""
def main(pathTxtFile):

        """Need to open the txt file"""
        openTxt = open(pathTxtFile, "r")
        text = openTxt.readlines()

        tempList = []

        for line in text:
                contact_instance = Contact(line)
                tempList.append(contact_instance)

        return tempList

if __name__ == "__main__":
        pass


