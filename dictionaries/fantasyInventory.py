
inventory = {}

def checkItemInv(item, inv):
    if item not in inv:
        return inv.setdefault(item, 0)
    else:
        return inv.get(item)

def checkFullInv(inv):
        for k, v in inv.items():
            print(str(v) + ' ' + k)
        print('')
    
def insertInv(item, qt, inv):
    if item not in inv:
        inv.setdefault(item, qt)
    else:
        inv[item] = int(inv[item]) + int(qt)
    print('Your inventory now contains:')
    checkFullInv(inv)
        

while True:
    print('What do you want to do? Insert, check, or nothing to leave')
    answer = input()
    if answer.lower() == 'check':
        print('Your inventory:')
        checkFullInv(inventory)
    elif answer.lower() == 'insert':
        print('What Item do you want to insert?')
        it = input()
        print('How many?')
        quantity = input()
        insertInv(it, quantity, inventory)
    else:
        break
