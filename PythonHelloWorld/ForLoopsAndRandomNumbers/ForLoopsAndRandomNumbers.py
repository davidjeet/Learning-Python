#import random
import sys # normal way of importing
from random import * #allows me not to worry about specifying namespace in front of commands. 

prev = 0
for i in range(10):
    #print(random.randint(1,10))
    x = randint(1,10)
    while x==prev:
        x = randint(1,10)
    print(x)
    prev = x

while True:
    print('To exit, you must type \'exit\'')
    response = input()
    if response == 'exit':
        sys.exit()

print("Freedom!!!!!!!!!!!!1")
# things to learn
#1. import statement brings in other modules