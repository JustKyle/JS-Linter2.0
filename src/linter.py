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
        if '{' in line:
            if(not re.match(".+\{\\n$", line)):
                print("%d. Open curly brace should not stand-alone." % lineNum)
        if '}' in line:
            if(not re.match("\}\\n$", line)):
                print("%d. Closing curly brace should stand-alone." % lineNum)
        if(re.match(".+(?<!=)==(?!=).+", line)):
            print("%d. Should only use strict equality." % lineNum)
        if(re.match(".*\".*\"", line)):
            if "'" not in line:
                print("%d. Should use single quotes." % lineNum)
        lastLine = line
    if(not re.match(".*\\n$", lastLine)):
        print("%d. File %s should end with a newline character." % (lineNum, sys.argv[1]))
js.closed
