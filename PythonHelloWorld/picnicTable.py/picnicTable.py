def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

#examples

items = { 'sandwichs' : 200, 'apples': 4, 'cookies' : 17, 'mangos' : 3 }
printPicnic(items, 12, 5)
printPicnic(items, 20, 6)