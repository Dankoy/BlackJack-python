import random

def toStr(listobj):
    string = ''
    listlen = len(listobj)
    for i in range(listlen):
        if i < listlen-1:
            string = string + str(listobj[i]) + ', '
        else:
            string = string + str(listobj[i])
    print(string)
    

 
spam = ['apples', 'bananas', 'tofu', 'cats']
randFloatList = list(random.uniform(1, 10) for i in range(random.randint(1, 100)))
randIntList = list(random.randint(43, 76) for i in range(random.randint(1,50)))

toStr(spam)
toStr(randFloatList)
toStr(randIntList)



