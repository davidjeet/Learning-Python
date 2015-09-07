#! python3
# phoneAndEmail.py - Find phone #'s and email address on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?  #separator
    (\d{3}) #first three digits
    (\s|-|\.)  #separator
    (\d{4}) #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #username
    @                  # @symbol     
    [a-zA-Z0-9.-]+ # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for email in emailRegex.findall(text):
    matches.append(email)
   # print(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
