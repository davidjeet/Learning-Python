print('Hello World')
print('What is your name?')
myName = input()
print("It is good to meet you, " + myName)
print('The length of your name is: ' + str(len(myName)))
print ('This is a single quote \' ')
x = 42.0 == '42' #false
print(not x)

#couple things to learn
#1. input() takes input form a user
#2. notice str(len(myName)). len returns an integer, and you cannot add an integer to a string so str 'casts' it
#3. can use double quotes or single quotes for strings (but the convention is single quotes)
#4. escaping is done via use of preceding \ character (line 6).
#5. types matter 7-8
#6. feels like c# w/o the semi-colons, braces and multiple parens!
#7. Logical operators are case-sensitive: and/or/not. Not AND/OR/NOT.
#8. Booleans are True and False. Not TRUE or FALSE.
#9. is an
