cat = ['fat', 'black', 'loud', 'sleepy']
#size = cat[0]
#color = cat[1]
#disposition = cat[2] # but this way is laborious....
size, color, disposition, fatigueLevel = cat
print(cat[1]) # should be black

spam = 42
spam +=1
print(spam) 

bacon = ['St.Lucia','Pitons']
bacon *= 3
print(bacon)

print(cat.index('loud')) # 2
print(cat[:2]) # everything up to 2
print(cat[1:2]) # The same as cat[1]
print(cat[-1]) # sleepy
print(cat[2:]) # Everything from index 2 onward
print(cat[:]) # Everything

print('*** Append,insert, remove,sort ***')
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam.insert(2, ' chicken')
spam.remove('dog')
del spam[0] 
print(spam)

spam = ['cat', 'dog', 'bat', 'elephant', 'bat', 'cat', 'rat','cat' ]
spam.remove('cat') #removes first instance
print(spam)

spam = ['cat', 'dog', 'bat', 'elephant', 'bat', 'cat', 'rat','cat' ]
spam.sort()
print(spam)
spam.sort(reverse = True)
print(spam)




# things to learn
#1. multiple assignemnt is powerful! (line 5)
#2. Lines 9 and 13 demonstrate augmented assignment operators
#3. Get the index of something in the list (line 16)
#4. sublists in 17 and 18,20
#5. -ve index lists. negative counts from -1 == last element, -2 == second to last, etc. (line 19)
#6. append, insert, remove behave as expected. del is a command that requires you know the index
#7. Sorting makes sense but word of warning: lists must have homogenous types (all strings, all ints, etc)
