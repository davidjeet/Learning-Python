spam  = "This is Alice's cat\n Ok???"
print(spam)
print(r'That is Carol\'s cat')

print('''Dear Alice

I am going to the store.

Best,
David''')

""" This is a Python multi-line
    comment.
    Please be respectful of it.
"""

x = 'cat' not in spam
print(x) # False, it is in spam 

#lower, upper, isupper, islower
print(spam.upper())
print(spam.lower())

spam= 'Hello World'
print(spam.isalnum()) #True
print(spam.isdecimal()) # False
print(spam.isdigit()) # False
spam='Hello'
print(spam.istitle()) # True (single word, capitalized first letter)

spam= 'Hello World'
print(spam.endswith('World')) # True
print(spam.startswith('Hel')) # True


# things to learn
#1. 'r' means raw string (ignore escapes). See line 3
#2. \n is a newline (line 1), \t is a tab and \\ is a backslash, etc.
#3. Triple quote means do a multiline paragraph. Cool! Lines 5, 10.
#4. Multiline line commends are just triple double quotes (lines 12,15)
#5. Strings can be indexed i.e. spam[3] returns a char. But you can't modify them




