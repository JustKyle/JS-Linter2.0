import re
import sys

with open(sys.argv[1], 'r') as js:
    lineNum = 0
    lastLine = ''
    for line in js:
        lineNum += 1
        if(re.match("\/\/.*", line) or re.match("^\s*$", line)):
            continue
        if(not re.match("^.*[\;|\}|\{]$", line)):
            print("%d. Statement should end with a semicolon." % lineNum)
        if(not re.match(".*[^\s+]$", line)):
            print("%d. Statement should not have trailing whitespace." % lineNum)
        lastLine = line
    if(not re.match(".*\\n$", lastLine)):
        print("%d. File %s should end with a newline character." % (lineNum, sys.argv[1]))
js.closed
