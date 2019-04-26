 
import random, sys

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('What is your wish?')
wish = input()
rand = random.randint(0, len(messages) - 1)
print(messages[rand])
