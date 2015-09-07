print('Give me a name, buddy')
name = input()

if name == 'David':
    print('Hi ' + name)
    print("Let's go to the mall")
elif len(name) > 5:
 print('that is a long name')
else:
    print('I know like you ' + name)

name = ''
i = 0
while name != 'david' and name != 'David':
    print('Please type your name.')
    name=input()
    i = i + 1
print('You escaped in ' + str(i) + ' tries!')



#couple things to learn
#1. indentation matters for blocks, but it can be tabs, spaces, 1 space. Tabs are just easier.
