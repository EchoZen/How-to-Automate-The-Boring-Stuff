# ? group matches 0 or 1 times
# * group matches 0 or more times
# + group matches 1 or more times
# {x} group matches x number of times
# {x,y} group matches x-y number of times
# Greedy matching: matches longest string possible
# Non-greedy matching: matches shortest string possible

import re
phoneNumRegex= re.compile(r'(\d\d\d-)?\d\d\d\d-\d\d\d')
mo= phoneNumRegex.search("My phone number is 415-5555-6767. Call me tmr.")
print(mo.group())
mo= phoneNumRegex.search("My phone number is 5555-6767. Call me tmr.")
print(mo.group())

#Greedy matching. It will take the longest between 3 and 7 
sillysentence= re.compile(r'(HA){3,7}')
mo= sillysentence.search("HAHAHAHAHA")
print(mo.group())