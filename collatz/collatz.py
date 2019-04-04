 
import sys

def collatz(num):
    while num != 1:
        num = num // 2
        print(num)
    return num

print('Input your number to collatz')

try:
    myNum=input()
    myNum=collatz(int(myNum))
except ValueError:
    print('You shall insert only integers')

    
