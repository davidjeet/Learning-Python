z = 'Demetrius Harris'
for i in z:
    print(i,end = '*')
print()
eggs = ('hello', 323, 0.5)
print(eggs[2])
#eggs[1] = 400 # illegal

#converting tuple to list
a = list(eggs)
a[1] = 500
b = tuple(a)
print(b)

spam = 42
cheese = 100
print(spam)
print(cheese) #different than spam, because by-value

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese) #should be identical, because lists are reference types

x = [[3,4,5,6],[7,8,9,10],9.1]
y = x.copy()
# z = x.deepcopy()
y[1] = 'blah'
print(x)
print(y)

# things to learn
#1. lists are mutable, strings are not. So z[2] = 'g' is illegal
#2. Tuples are like lists but use parens() not square brackets. 
#3. Tuples are also immutable. (line 7)
#4. Use tuples to signal you don't want data changed, 
#   also it optimzes Python for speed working with these. 
#5. convert to tuples/lists using list() and tuple(). See 10, 12
#6. variables are by-value, but lists are by reference 


