import os
path = os.path.join("C:\\", 'Python','PythonHelloWorld','ReadingAndWritingFiles')
print(path)

print(os.getcwd())

#creates all necessary folders if they don't exist
path = 'C:\\temp\\junker\\deleteme'
if not os.path.exists(path):  #an error if deleteme folder already exists
    os.makedirs(path)
    print(path + ' was created.')
else:
    print(path + ' already exists!')   

current = os.getcwd()
print(os.listdir(current))
print(os.path.getsize(current))

winPath ='C:\\Python34'
totalsize = 0
for filename in os.listdir(winPath):
    totalsize = totalsize + os.path.getsize(os.path.join(winPath, filename))

print(str(totalsize) + ' bytes')


#path = 'C:\\temp\\hello.txt'

#path = 'C:\\temp\\h1.txt'
#if (os.path.exists(path)):
#    print('yess')
#else:
#    print('no')

helloFile = open('hello.txt')
content = helloFile.readlines()
helloFile.close()
print(content)

baconFile = open('c:\\temp\\bacon2.txt', 'w')
baconFile.writelines('Bacon is not a veggie\nNot it is not.\n')
baconFile.close()

baconFile = open('c:\\temp\\bacon2.txt', 'a')
baconFile.writelines('I love all foods, including bacon    !!!!1.\n')
baconFile.close()

baconFile = open('c:\\temp\\bacon2.txt')
content = baconFile.readlines()
baconFile.close()
print(content)




# things to learn
#1. c:\windows\system32\calc.exe : dir name is first part, base name is calc.exe
#2. invoke using os.path.basename(..) or os.path.dirname(...)
#3. os.path.exists, .isdir, .isfile are pretty much straightforward

