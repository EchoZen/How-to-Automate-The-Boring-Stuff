# Regular expressions help you match/find other strings or sets of strings
import re
message= "Call me 415-555-0000 tomorrow, or at 367-346-7777"
# Usually use raw strings, r''
# Raw strings ignore \ functions. eg. \n will no longer create new line. It will literally be a string
# \d is to find digits
# The matching of the pattern will be stored into the variable
phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo are match objects
mo= phoneNumRegex.search(message)
print(mo.group())
print(phoneNumRegex.findall(message))

# Grouping
# Use brackets to group
phoneNumRegex= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
hello= phoneNumRegex.search(message)
print(hello.group())
print(hello.group(1))
print(hello.group(2))

# finding literal brackets (), not grouping, use \
phoneNumRegex= re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')
hello= phoneNumRegex.search(message)
hello1= phoneNumRegex.search("Call me (415)-555-0000 tomorrow, or at 367-346-7777")
print(hello) #This will give none as there's no brackets in original message
print(hello1.group())

# Pipes= |
# Acts like 'or'. Can match one of many possible groups
batRegex= re.compile(r'Bat(man|woman|mobile|copter|hat)')
mo= batRegex.search("Batmobile lost a wheel")
print(mo.group())
# If string is not matched, none will be returned.
# Note! This can cause error in programs that call the function
mo= batRegex.search("Batmotorcycle lost a wheel")
print(mo)
