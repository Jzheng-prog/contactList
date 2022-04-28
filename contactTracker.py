
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
        addfind = re.findall("\w+\w+\w",singleContactLine)
        return addfind

"""Derek"""
def parsePhoneNum(singleContactLine):
        phofind = re.findall("\w+\w+\w",singleContactLine)
        return phofind




"""MyContackList class will have a list of contact objects, and can manipulate/sort contact Objects"""
class MyContactList:
        def __init__(self, allCONTACTFILE):

                """Create a contactList"""
                self.contactList = []
                """Open and read the file parameter"""
                opentxt = open(allCONTACTFILE, "r")
                readtxt = opentxt.read()

                """Construct regex pattern and search for it in the file"""
                contactPattern = re.compile(r"[s\S]*?(com|edu|net")
                searchPattern = contactPattern.search(readtxt)

                """Use loop to break the file into individual Contact objects, and append to list"""
                for contacts in searchPattern:
                        contactObj = Contact(contacts)
                        self.contactList.append(contactObj)


        """"Sort the list""""""John"""
        def sortList():
                pass


def main(pathTxtFile):
        pass

if __name__ == "__main__":
        pass


