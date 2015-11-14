import re

with open(sys.argv[1], 'r') as js:
    lineNum = 0
    for line in js:
        if(re.match("\/\/.*", line)):
            lineNum++
            continue
        if(!re.match(".*;|{$", line)):
            print ('%d. Statement should end with a semicolon.', lineNum)

        lineNum++
js.closed
