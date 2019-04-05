import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count) 
print(count.items())
print(count.keys())
print(count.values())

for k,v in count.items():
    print('The key: ' + k + '. The value: ' + str(v))
    
    
pprint.pprint(count)
