
from ast import arg
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

        def __init__(self):
                """Create a contactList"""
                self.contactList = []

        """return list as a string"""
        def __repr__(self):
                pass



def main(pathTxtFile):

        """Open and read the file parameter"""
        opentxt = open(pathTxtFile, "r")
        readtxt = opentxt.read()

        """Construct regex pattern and search for contacts in the file"""
        pattern = re.compile(r".+\n.+\n.+\n.+\n.+\n.+\n.+\n.+")

        matches = pattern.findall(readtxt)

        """"Create a MyContactList Object"""
        myContactList_instance = MyContactList()

        """Use loop to break the file into individual Contact objects, and append to list"""
        for contacts in matches:
                
                """for each contacts in searchPattern, create an new contact obj"""
                contactObj = Contact(contacts)
                """Then append to the list_instance list"""
                myContactList_instance.contactList.append(contactObj)

        print(myContactList_instance)

def parse_args(args_list):

        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type = str, help = 'The path of samConList.txt.')
        args = parser.parse_args(args_list)
        return args


if __name__ == "__main__":
        args = parse_args(sys.argv[1:])
        main(arg.pathTxtFile)


