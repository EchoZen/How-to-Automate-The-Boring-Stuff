# ^ means the string must start with the pattern
# $ means string must end with the pattern
# . is anything except new lines \not
# pass re.DOTALL as second argument to re.compile() to make the dot match new lines as well
# pass re.I as second argument to re.compile to make matching case insensitive
import re
beginswHelloregex= re.compile(r'^Hello')
print(beginswHelloregex.search("Hello"))
print(beginswHelloregex.search("My name is Hello")) # prints None value as Hello is not the start of the string
endswworldregex= re.compile(r'world!$') # as long as string ends with world, there will be a match
print(endswworldregex.search("Hello world!"))

# Use both ^ and $ means must match entire string
alldigitsregex= re.compile(r'^\d+$') # The entire string can only contain numbers
print(alldigitsregex.search('12345685436543'))
print(alldigitsregex.search('1234568x5436543')) # will output none because no string matches both ^$

atregex= re.compile(r'.at')
print(atregex.findall("The cat with a flat hat sat on a mat ")) # Does not print 'flat', prints 'lat'

atregex= re.compile(r'.{1,2}at')
print(atregex.findall("The cat with a flat hat sat on a mat ")) # prints 'flat' now, but also prints the spaces

name= "First name: Zoe Last name: Chen Hui Xin"
# .* means will find ANYTHING. it is grouped (), so will only find the groups that have first name and last name
nameregex= re.compile("First name: (.*) Last name: (.*)")
print(nameregex.findall(name)) # Will give tuples

# .*? to use nongreedy match
serve= '<To serve humans> for dinner.>'
nongreedy= re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))