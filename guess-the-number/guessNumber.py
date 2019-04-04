
import random, sys

def checkNum(num):
    global cNum
    if num < cNum:
        print('Your number is too low')
    elif num > cNum:
        print('Your number is too high')
    elif num == cNum:
        print('You guessed right')
        sys.exit()
        
print('I am thinking of a number between 1 and 10.\n')
cNum = random.randint(1, 10)

while True:
    print('Take a guess:')
    try:
        myNum=input()
        checkNum(int(myNum))
    except ValueError:
        print('You must enter integers!')
    
