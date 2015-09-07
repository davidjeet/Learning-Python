import re

#basic regex with groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242.")

print(mo.group(0))
print(mo.groups()) # two groups
print(mo.group(1)) # first three digits because they are in parens
print(mo.group(2)) # second group xxx-xxxx because they are in parens
areacode, mainNumber = mo.groups()
print(areacode)
print(mainNumber)

# matching multiple groups with pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey, and Jeff')
print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|crap)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# Optional matching with the question mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# There is matching with * (or more) and + (one or more)
# I'm not going to repeat that commonly understand aspect of regex here.

#Greedy matching
#Python is greedy by default so it will match the longest
#In the second example it matches the shortest by the use of '?' (unreleated to 0/1 usage)
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nogreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nogreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

#findall
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #no groups in regex 
mo = phoneNumRegex.findall("My work number is 415-555-4242 and my home is 212-736-9909.")
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #groups in regex 
mo = phoneNumRegex.findall("My work number is 415-555-4242 and my home is 212-736-9909.")
print(mo) #groups no visible in result

newLineRegex = re.compile('.*', re.DOTALL)
x = newLineRegex.search('Strength and Honor\nWildcat Way.\nWin on three.')
print(x)

namesRegex  = re.compile(r'Agent \w+')
x = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(x)

#Other concepts
#1. defining what you allow ex. => r'[aeiouAEIOU'] matches all vowels, better than \w
#2. ^ for begings with and $ for ends with
#3. The . character is a wildcard that matches any character except a newline
#4. Match everything .* (except newline). It does this in greedy fashion.
#5. (.*?) is match everything not greedy.
#6. complex regex take advantage of ''' to split out regex to make it more redable [p.164]
