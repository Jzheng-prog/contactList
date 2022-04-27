
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
    def __init__(self, contactList):
        self.name = parseName(contactList)
        self.email = parseEmail(contactList)
        self.address = parseAddress(contactList)
        self.PhoneNum = parsePhoneNum(contactList)

"""Functions below helps us parse throught he context to fine the information we want"""

"""Bushrah"""
def parseContact(contactList):
        pass
"""Bushrah"""
def parseName(contactList):
        pass

"""John"""
def parseEmail(contactList):

        pattern = re.compile(r"\w+@\w+.+")
        match = pattern.search(contactList)
        return match

"""Derek"""
def parseAddress(contactList):
        pass
"""Derek"""
def parsePhoneNum(contactList):
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



if __name__ == "__main__":

        """Need to open the txt file"""
        openTxt = open(ContactList, "r")
        contactInstance = Contact()


