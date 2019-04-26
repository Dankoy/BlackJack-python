import shelve

# write in shelve file
shelveFile = shelve.open('/home/ezelenin/git/python-learning/Files/mydata')
listCats = ['cat1', 'cat2', 'cat3']
shelveFile['cats'] = listCats
shelveFile.close()

# read from shelve file
shelveFile = shelve.open('/home/ezelenin/git/python-learning/Files/mydata')
takeBack = shelveFile['cats']
print(type(takeBack))
print(takeBack)
shelveFile.close()
