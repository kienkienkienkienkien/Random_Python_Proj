import re
from re import search
word = "postion"
minusPos = -1


inpu = input("input: ")
for match in re.finditer(inpu, word):
    minusPos = match.start()
    print(minusPos)