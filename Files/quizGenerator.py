import random, os, sys

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
   'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
   'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

question = 'What is the capital of '

for i in range(35):
    if not os.path.exists('./quizes/'):
        os.mkdir('./quizes/')
    else:
        fileOpen = open('quizes/quiz'+str(i+1), 'w')
        for j in range(50):
            state, city = random.choice(list(capitals.items()))
            fileOpen.write(str(j+1) + '. ' + question + state + '\n')
            listOf = [city]
            
            # Put random answers in list and shuffle it for random printing
            for k in range(3):
                listOf.append(random.choice(list(capitals.values())))
            random.shuffle(listOf)
            
            for n in range(4):
                fileOpen.write('\t' + str(n+1) + ') ' + listOf[n] + '\n')
                
        fileOpen.close()
        
        
        
        
        
