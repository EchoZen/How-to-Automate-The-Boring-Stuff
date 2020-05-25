import pyperclip, re

# Create phone regex
phoneRegex= re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?    # area code (opt)
(\s|-)                      # 1st separator
\d\d\d                      # 1st 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word part (opt)
(\d{2,5}))?)                   # extension number part (opt)
''', re.VERBOSE)

# Create email regex
emailRegex= re.compile(r'''
[a-zA-Z0-9_.+]+ # inside your own class, don't need to backslash
@
[a-zA-Z0-9_.+]+''', re.VERBOSE|re.DOTALL)

# Get text off clipboard
text= pyperclip.paste()

# Extract email/phone through text
extracted_phone= phoneRegex.findall(text)
extracted_email= emailRegex.findall(text)
allphonenumbers=[phone_number[0] for phone_number in extracted_phone]
print(allphonenumbers)
print(extracted_email)

# Copy extracted email/phone to clipboard
results= '\n'.join(allphonenumbers)+ '\n'+ '\n'.join(extracted_email)
pyperclip.copy(results)