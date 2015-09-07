import pprint

myCat = { 'size' : 'fat', 'color' : 'gray', 'age' : 2 }
myCat2 = { 'size' : 'fat', 'color' : 'gray', 1000 : 2, True : 99 }

print(myCat)
print(myCat2['size'])
print(myCat2[1000])
print(myCat2[True])
# print(myCat2[0]) #illegal because a key of 0 does not exist

birthdays = { 'David': 'Sep 14', 'Jon': 'Sep 28', 'Stacie': 'Apr 17' }
while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have this name in our database")
        print("What is their birthday?")
        bday  = input()
        birthdays[name] = bday

pprint.pprint(birthdays)

for item in birthdays.keys():
    print(item)

for item in birthdays.items():
    print(item)

for item in birthdays.values():
    print(item)

items = {'apples':5, 'cups':2 }
print ('I am bringing ' + str(items.get('cups',0)) + ' cups.' )
print ('I am bringing ' + str(items.get('eggs',0)) + ' eggs.' )

spam = { 'name': 'Pooka', 'age' : 5 }
spam.setdefault('color', 'black')
print(spam)


#things to learn
#1. dictionaries use curly parens (different from tuples and lists)
#2. keys can be strings, floats, ints, booleans
#3. keys(), values(), items() are straightforward 26, 29, 32
#4. get() takes two arguments and returns a value if it exists or the value of second
#   argument if it doesn't. Just a more concise way of doing things
#5. pretty print requires library pprint (line 1, 26)
