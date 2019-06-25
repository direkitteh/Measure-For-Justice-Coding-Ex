# Laura Durant
# Measures For Justice Coding Eval
# Parse Data
# 4/23/19

# In this exercise I use double quotes to escape ambiguous commas

import io
import re

def readFile(filename):
    file = open(filename, 'r')
    return file.read()

# The fixes for various lengths are largely guesswork based on patterns.
# A better way to do this is to track the properly formatted names and
# identify them within the incorrect data. The set was small enough for
# me to use patterns to rough out a solution rather than attempt some
# kind of light AI to identify name groupings.
def fix(fields):
    count = len(fields)
    if count is 0:
        return
    if count is 1 and not fields[0]:
        return
    isNum = []
    notNum = []
    for field in fields:
        if re.search("[0-9][0-9][0-9]", field):
            isNum += [field]
        else:
            notNum += [field]
    #isNum is always length 3
    if len(notNum) is 2:
        #no attorney listed
        fields.insert(3,"")
        return fields
    if len(notNum) is 6:
        # most likely "last, first, suffix, attorney last, attorney first, desc"
        # handle suffixing in the 4 case instead of rewriting the code here
        notNum = [notNum[1] + ' ' + notNum[0],notNum[2],notNum[4] + ' ' + notNum[3], notNum[5]]
    if len(notNum) is 4:
        # if both have spaces, assume it's a suffix for the first name
        if ' ' in notNum[0] and ' ' in notNum[2]:
            notNum = ['"' + notNum[0] + ', ' + notNum[1] + '"',notNum[2],notNum[3]]
        # if only the first name has a space, assume it's part of the attorney name
        elif ' ' in notNum[0]:
            notNum = [notNum[0],notNum[2] + ' ' + notNum[1],notNum[3]]
        # if only the second name has a space, assume it's part of the first name
        elif ' ' in notNum[2]:
            notNum = [notNum[1] + ' ' + notNum[0], notNum[2],notNum[3]]
        # no other cases occur in this set
    if len(notNum) is 5:
        # it's probably two names in "last, first" style
        notNum = [notNum[1] + ' ' + notNum[0],notNum[3] + ' ' + notNum[2],notNum[4]]
    #notNum is never >6
    if len(isNum) is not 3 or len(notNum) is not 3:
        # I'd have to add more handling since this is more manual fixing than algorithmic
        print("Something has gone amiss...")
    # put the fields together
    return [isNum[0],isNum[1],notNum[0],notNum[1],isNum[2],notNum[2]]

content = readFile("fakedata.csv").split("\n")
lines = []
for line in content:
    fields = []
    start = 0
    inQuote = False
    for i in range(len(line)):
        if line[i] is '"':
            if inQuote:
                if line[i+1] is '"':
                    i += 1
                else:
                    inQuote = False
            else:
                inQuote = True
        elif line[i] is ',':
            if not inQuote:
                fields += [line[start:i]]
                start = i+1
    fields += [line[start:]]
    if len(fields) is not 6:
        fields = fix(fields)
    if fields:
        lines += [fields]

f = open("valid.csv", 'w')
for line in lines:
    f.write(str.join(",", line)+"\n")
