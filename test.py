import re

str = "<AX, {<e1, 10>, <e2, 5>}>"

print(re.search("(?<={).+(?=})", str).group())