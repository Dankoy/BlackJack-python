 
import sys

array = []
while True:
    print('Do you want to read from array or insert in array?')
    answer=input()
    if answer == 'insert':
        print('What do you want to insert in array?')
        word=input()
        array.append(word)
    elif answer == 'read':
        for i in array:
            print(' ' + i)
    elif answer == 'check':
        print('Check what?')
        word=input()
        if word not in array:
            print('Word not in array')
        else:
            print('Word is in array ' + word + ' and it\'s index is ' + str(array.index(word)))
    elif answer == 'remove':
        print('What do you want to insert in array?')
        word=input()
        try:
            array.remove(word)
            print('Removed')
        except ValueError:
            print('This word is not in list')
    elif answer == '':
        break
