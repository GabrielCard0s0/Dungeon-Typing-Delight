from listas import weaponmelee, initialmove, moves, inventory
import time
import sys
import random

def main():
    time.sleep(1)
    print('-'*30)
    print('Select an option:\n', '1. Start Game\n', '2. Exit')
    print('-'*30)
    option = int(input())

    time.sleep(1)

    if option == 1:
        print('-'*30)
        print('Starting...')
        print('-'*30)
        return Initial()
    elif option == 2:
        print('-'*30)
        print('Ending...')
        print('-'*30)
        sys.exit()
    else:
        return main()

def Initial():
    print(initialmove)
    print(random.choices(moves, k=1))
    time.sleep(1)
    print(random.choices(moves, k=1))
    time.sleep(1)
    print(random.choices(moves, k=1))
    time.sleep(1)
    return InitialWeapon()
    
def InitialWeapon():
    print('You have found a chess!')
    #ainda em desenvolvimento
    #preciso que o bau mostre 3 weapon melee
    #preciso que o usuario possa escolher dentre as 3 armas e que ela vá para o inventario

print('-'*30)
print('Welcome to Dungeon Python!')
print('-'*30)
main()