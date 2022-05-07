import re

f = open("samConList.txt", "r")

readTXT = f.readlines()

pattern = re.compile(r".+\n.+\n.+\n.+\n.+\n.+\n.+\n.+")

match = pattern.finditer(str(readTXT))

tempList = []

for line in match:
    print(line)




