
import re
import sqlite3
import sys
import argparse

"""We will have a list of contacts, with the names, emails, phone number, and addresses. This could be one or more. We will parse
through the list, break them up into individual objects, and then we can have different methods/functions
to organized them base on the broken parts, for example
we can break organized them by name (alphabetacle order) or by phone number."""


"""One contact object contains names, emails, phone number, and addresses. There will be a list of contact objects in another class 
called MyContactList."""
class Contact:

        """would use parse functions to find each atrribute of the contact"""
        def __init__(self, singleContactLine):
                self.name = parseName(singleContactLine)
                self.email = parseEmail(singleContactLine)
                self.address = parseAddress(singleContactLine)
                self.PhoneNum = parsePhoneNum(singleContactLine)

"""Functions below helps us parse through the text to find the information we want"""


"""Bushrah"""
def parseName(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)")
        match = pattern.search(singleContactLine)
        return match.group(1)

"""John"""
def parseEmail(singleContactLine):
        
        pattern = re.compile(r".+?@.+")
        match = pattern.search(singleContactLine)
        return match

"""Derek"""
def parseAddress(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)")
        match = pattern.search(singleContactLine)
        return match.group(2,3,4,5)


"""Derek"""
def parsePhoneNum(singleContactLine):
        pattern = re.compile(r"Contact \d:(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)(\n.+)")
        match = pattern.search(singleContactLine)
        return match.group(6)


"""MyContackList class will have a list of contact objects, and can manipulate/sort contact Objects"""
class MyContactList:
        def __init__(self, allCONTACTFILE):

                """Create a contactList"""
                self.contactList = []
                """Open and read the file parameter"""
                opentxt = open(allCONTACTFILE, "r")
                readtxt = opentxt.read()

                """Construct regex pattern and search for it in the file"""
                contactPattern = re.compile(r"[s\S]*?@.+")
                searchPattern = contactPattern.search(readtxt)

                """Use loop to break the file into individual Contact objects, and append to list"""
                for contacts in searchPattern:
                        contactObj = Contact(contacts)
                        self.contactList.append(contactObj)


def main(pathTxtFile):
        pass

if __name__ == "__main__":
        pass


