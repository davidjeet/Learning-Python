a = [1,3,5,7]
b = ['jeff', 5.1, True, 400]

print(a)
print(b)
c =  a + [9]
print(c)
print(b[2]) 

d= [['sword', 'flail'],[10, 20, 30, 40], True, 9999.1]
print(d[0][1]) # flail
print(d[3]) # 9999.1
print(len(d))
print(d[1])
d[1][2] = 70
print(d[1])
e = a + a
print(e)

catNames = []
while True:
        print('Enter name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.:')
        name = input()
        if name == '':
            break;
        catNames = catNames + [name] #list contatenation!!!
print('The cat names are:')
for name in catNames:
    print(' ' + name)


print('jeff' in b)
print('Jeff' in b)
print(5.1000 in b)

# things to learn
#1. lists are square bracket sequences
#2. lists are not strongly typed...you can mix up types in a list (see line 2)
#3. lists can only concatenante to lists (line 6)
#4. Lists are zero-based arrays
#5. Lists can contain lists (line 11)
#6. You can modify an array by accessing it's index directly (line 15)
#7. Whoa...a foreach loop (line 28)
#8. Notice list concatnenation with a single variable means it has it to be list-ified (line 26)
#9. Empty list declaration on line 20.
#10. Basically arrays in Python are mutable C# lists
