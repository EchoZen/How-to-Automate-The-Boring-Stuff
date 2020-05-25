import re
namesRegex= re.compile(r'Agent \w+')
agent= namesRegex.findall('Agent Alice is looking for Agent Bob.')
print(agent)
# sub method: find and replace method (substitute words)
# first argument is what you want to replace it with
agent= namesRegex.sub('Redacted', 'Agent Alice is looking for Agent Bob.')
print(agent)

# To replace only part of the regex
namesRegex= re.compile(r'Agent (\w)\w*')
# 1st argument is what you want to substitute
# \1 refers to group 1 of regex
# Ouput is Agent + 1st letter of the word
agent= namesRegex.sub(r'Agent \1***',r'Agent Alice is looking for Agent Bob.')
print(agent)

# Verbose
# Lets you write comments in your regex
phoneRegex= re.compile(r'''
\d\d\d      # Area code
-           # 1st dash
\d\d\d      # 1st 3 digits 
-           # 2nd dash 
\d\d\d\d    # last 4 digits
\sx\d{2,4}  # extension code
''', re.VERBOSE|re.I|re.DOTALL)
# re.I ignores case when searching for something
# DOTALL includes '.' as part of literal search
# Only 1 argument allowed after the raw string,
# Have to combine re.VERBOSE, re.I and re.DOTALL with '|' operator
