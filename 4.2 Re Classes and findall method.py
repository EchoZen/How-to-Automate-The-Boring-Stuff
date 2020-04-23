import re

# Regex method findall() is passed a string and returns all matches
# If regex has 0 or 1 groups, findall() returns a list of strings
# If regex has 2 or more groups, findall() returns a list of tuples of strings
# Classes
# \d is a shorthand character class for matching digits
# \s for spaces, tabs, new lines
# \w for characters, digits and underscores
# \D, \S, \W is for anything BUT those
# You can make your own character class with []
# To use negative character classes, add ^ infront [^]
resume= '''David Leonne
Sometown, MA 55555 | 555-555-5555 | dl@somedomain.com | LinkedIn URL | 678-555-3344 '''
phoneRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # No grouping
phone_numbers= phoneRegex.findall(resume)
print(phone_numbers)

phoneRegex= re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d') # 1 group
phone_numbers= phoneRegex.findall(resume)
print(phone_numbers)


phoneRegex= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # 2 groups
phone_numbers= phoneRegex.findall(resume)
print(phone_numbers) #prints list of tuples of strings

# To include the dash
phoneRegex= re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))') # 3 groups
phone_numbers= phoneRegex.findall(resume)
print(phone_numbers) # 1st grp: outer brackets. 2nd grp: next bracket. 3rd grp: last bracket

# \d is the same as using digits 0-9 with pipe |
number= re.compile(r'\d')
numbers = number.findall(resume)
print(numbers)

number= re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
numbers = number.findall(resume)
print(numbers) # Same outcome but more effort

# Example: 12 days of christmas
christmas_song= '''12 drummers drumming
11 pipers piping
10 lords a leaping
9 ladies dancing
8 maids a milking
7 swans a swimming
6 geese a laying
5 gold rings, badam-pam-pam
4 calling birds
3 French hens
2 turtle doves
And 1 partridge in a pear tree'''
# Get number and 1st word
song= re.compile(r'\d+\s\w+') # + will match until there's no more to match
print(song.findall(christmas_song))

#Create own character classes
vowelRegex= re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u), but simpler
# Can also use -. eg. r'[a-z]' will find all alphabets
print(vowelRegex.findall("Baby Zoe wants to eat food."))

doublevowelRegex= re.compile(r'[aeiouAEIOU]{2}') # Only find those with x consecutive no. of times
print(doublevowelRegex.findall("Baby Zoe wants to eat food."))

vowelRegex= re.compile(r'[^aeiouAEIOU]') # everything BUT the vowels. Includes spaces and digits
print(vowelRegex.findall("Baby Zoe wants to eat food."))
