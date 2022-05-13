import re

"""Test scanning for one contact in a list of contacts"""

f = open("samConList.txt", "r")

readTXT = f.read()

pattern = re.compile(r".+\n.+\n.+\n.+\n.+\n.+\n.+\n.+")

match = pattern.findall(readTXT)

tempList = []

for contact in match:
    tempList.append(contact)

print("The contact amount:" + str(len(match)))
print(tempList)






