import shelve
import pprint

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Jeet', 'Simoneon', 'Ana3', 'Mia2']
shelfFile['cats'] = cats
shelfFile['dog'] = 'Maggie Jeet'
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
for key in shelfFile.keys():
    print('KEYS: ' + key)

for value in shelfFile.values():
    print(type(value))
    print('VALUES: ' + ','.join(value))

shelfFile.close()

cats  = [{'name' : 'Jeet', 'desc' : 'Chubby thang description...'},   
         {'name' : 'Bolo Yeung', 'desc' : 'Shootfighter!'}]
fileObj = open('myCats.py', 'w')
fileObj.writelines('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
print(myCats.cats)
print(myCats.cats[0]['desc'])


#Things to learn

#1  Shelf files allow you to store KV dictionaries to be used like a configuration file.
#2. Holy crap, that's insane...I just wrote my own module in line 21-25. 
#   Then I imported it in 27 and called it in 28
