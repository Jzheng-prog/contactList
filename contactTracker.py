
"""We will have a list of contacts, with the names, emails, phone number, and addresses. This could be one or more. We will parse
through the list, break them up into individual objects, and then we can have different methods/functions
to organized them base on the broken parts, for example
we can break organized them by name (alphabetacle order) or by phone number."""


"""One contact object contains names, emails, phone number, and addresses. There will be a list of contact objects."""
class contact:

    def __init__(self, contactList):
        self.name = parseName(contactList)
        self.email = parseEmail(contactList)
        self.address = parseAddress(contactList)
        self.PhoneNum = parsePhoneNum(contactList)

"""Functions below helps us parse throught he context to fine the information we want"""
def parseContact(contactList):
        c = "etc"
def parseName(contactList):
        pass
def parseEmail(contactList):
        pass
def parseAddress(contactList):
        pass
def parsePhoneNum(contactList):
        pass

"""Add the contact object to a list of contacts"""
def addContactToList():
        pass
""""Sort the list"""
def sortList():
        pass
    


def main():
    pass

if __name__ == "__main__":
    print
    pass


