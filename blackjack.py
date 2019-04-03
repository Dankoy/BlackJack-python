#Simple program to play black jack
 
import random, sys

ptotal=0
dtotal=0
while True:
    print('Player\'s turn.\n')
    pt = random.randint(1, 11)
    dt = random.randint(1, 11)
    
    ptotal=ptotal+pt
    dtotal=dtotal+dt
    
    print('Your hand: ' + str(ptotal))
    print('Dealer\'s hand: ' + str(dtotal))
    
    
    while True:
        print('Do you need more? Type yes or no')
        panswer = input()
        if panswer == 'yes':
            while panswer == 'yes':
                pt = random.randint(1, 11)
                ptotal=ptotal+pt
                print('Your hand: ' + str(ptotal))
            
                if dtotal <= 20:
                    dt = random.randint(1, 11)
                    dtotal = dtotal + dt
                    print('Dealer\'s hand: ' + str(dtotal))
                else:
                    print('Dealer\'s hand: ' + str(dtotal))
                    
                print('Do you need more? Type yes or no')
                panswer = input()
                if panswer == 'yes':
                    continue
                elif panswer == 'no':
                    while dtotal <= 20:
                        print('Your hand: ' + str(ptotal))
                        dt = random.randint(1, 11)
                        dtotal = dtotal + dt
                        print('Dealer\'s hand: ' + str(dtotal))
                    
                    print('\nTotal hands:\nYour\'s ' + str(ptotal) + '\nDealer\'s ' + str(dtotal))
                    if ptotal <= 21 and ptotal > dtotal:
                        print('You win')
                        sys.exit()
                    elif ptotal > 21:
                        print('You lose')
                        sys.exit()
                    elif ptotal <= 21 and dtotal > 21:
                        print('You win')
                        sys.exit()
                
            
            
            
            
