#Simple program to play black jack
 
import random, sys

# Method to increase dealer's hand
def incDhand(dtotal):
    if dtotal <= 20:
        dt = random.randint(1, 11)
        dtotal = dtotal + dt
        return dtotal
    else:
        return dtotal

# Method to increase player's hand
def incPhand(ptotal):
    pt = random.randint(1, 11)
    ptotal=ptotal+pt
    return ptotal

# Method to decide winner
def whois(ptotal, dtotal):
    if ptotal <= 21 and ptotal > dtotal:
        return 'You win'
    elif dtotal > 21 and ptotal > 21:
        return 'Nobody wins'
    elif ptotal > 21:
        return 'You lose'
    elif ptotal <= 21 and dtotal > 21:
        return 'You win'
    elif dtotal == 21 and ptotal < 21:
        return 'You lose'
    


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
                ptotal=incPhand(ptotal)
                dtotal=incDhand(dtotal)
                print('Your\'s hand ' + str(ptotal)) 
                print('Dealer\'s hand ' + str(dtotal))
                
                print('Do you need more? Type yes or no')
                panswer = input()
                if panswer == 'yes':
                    continue
                elif panswer == 'no':
                    dtotal=incDhand(dtotal)
                    print('Dealer\'s hand ' + str(dtotal))
            
                print('\nTotal hands:\nYour\'s ' + str(ptotal) + '\nDealer\'s ' + str(dtotal))
            
        elif panswer == 'no':
            dtotal=incDhand(dtotal)
            print('\nTotal hands:\nYour\'s ' + str(ptotal) + '\nDealer\'s ' + str(dtotal))
            if dtotal <= 20:
                continue
            else:
                winner=whois(ptotal, dtotal)
                print(winner)
                sys.exit()
            
        
            
            
            
            
            
            
            
