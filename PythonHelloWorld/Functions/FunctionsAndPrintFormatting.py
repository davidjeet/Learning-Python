def SayHi(name):
    val = 'Hello ' + name
    return val

print(SayHi('David'))
val = print('xyz')
None == val


print('Lion','Nion','Zion!')
print('RavenDB', 'MongoDB', 'Riak', end='|')
print('Apache Cassandra')

def spam():
    print('Local spam(): ' + str(eggs))
eggs = 42
spam()
print('Global: ' + str(eggs))

def spam2():
    global eggs
    eggs = 35
    print('Local spam2(): ' + str(eggs))
eggs = 42
spam2()
print('Global: ' + str(eggs))


# Things to learn
#1. None is a special value. It's like null, or nil, or undefined in other languages
#2. by default the end parameter is ' ' . But in the example above I made it pipe
#3. This is not a statically typed language...notice I'm calling for eggs in spam but allowing the
#   interpreter to run without eggs being defined until after the function is defined!
#4. Notice, in order to modify a global variable you need to use the keyword 'global. See line 22


