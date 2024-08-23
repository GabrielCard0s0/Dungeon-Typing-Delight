import time, sys, random, colorama
from listas import weaponmelee, initialmove, moves, inventory, walkinfo, current_location, follow
from colorama import *

def main():
    time.sleep(1)
    print('-'*30)
    print('Select an option:\n', Fore.GREEN + '1. Start Game\n' + Style.RESET_ALL, Fore.YELLOW + '2. Exit' + Style.RESET_ALL)
    print('-'*30)
    option = int(input('Type the option: '))

    time.sleep(1)

    if option == 1:
        print('-'*30)
        print('Starting...')
        print('-'*30)
        return Initial_Step()
    elif option == 2:
        Ending()
    else:
        print('-'*30)
        print('Invalid option. Please try again.')
        return main()

def Get_Random_walkinfo():
    return random.choice(walkinfo)
    
def Ending():
    print('-'*30)
    print('Ending...')
    print('-'*30)
    sys.exit()

def Initial_Step():
    time.sleep(1)
    print('...Lets get started right away:')
    print(initialmove)
    print(random.choices(moves, k=1))
    time.sleep(1)
    print(random.choices(moves, k=1))
    time.sleep(1)
    print(random.choices(moves, k=1))
    time.sleep(1)
    return Chest_Event()
    
def Chest_Event():
    time.sleep(2)
    print('-'*30)
    print('You have found a chest!')
    print('-'*30)
    weapons = random.sample(sorted(weaponmelee), 3)
    print('-'*30)
    print('You found the following weapons:')
    print('-'*30)
    for i, weapon in enumerate(weapons, 1):
        print('-'*30)
        print(f'{i}. {weapon}')
        print('-'*30)
    choice = int(input('Choose a weapon: ')) - 1
    chosen_weapon = weapons[choice]
    print('-'*30)
    print(f'You chose the {chosen_weapon}')
    print('-'*30)
    inventory.append(chosen_weapon)
    return WalkChoice()

def move_player(direction):
    global current_location
    if direction == 1:
        current_location = follow[0]
    elif direction == 2:
        current_location = follow[1]
    elif direction == 3:
        current_location = follow[2]
    elif direction == 4:
        current_location = follow[3]
    else:
        print("Invalid direction. Please try again.")

def manage_inventory():
    print("You have the following items in your inventory:")
    for item in inventory:
        print(item)
    return WalkChoice()

def WalkChoice():
    time.sleep(1)
    print('-'*30)
    print(Get_Random_walkinfo())
    print('-'*30)
    print('You have the following options:')
    print('-'*30)
    print(f'\n1. Current Location\n 2. Follow to...\n 3. inventory\n 4. Exit Game\n')
    choice = int(input('Choose an option: '))
    if choice == 1:
            time.sleep(1)
            print('-'*30)
            print(current_location)
            time.sleep(1)
            return WalkChoice()
    elif choice == 2:
        print('-'*30)
        print(f'1. Go to north\n 2. Go to south\n 3. Go to east\n 4. Go to west')
        direction = int(input('Choose a direction: '))
        move_player(direction)
        print(f'You are now in the {current_location}')
        if current_location == 'South':
            pass
        elif current_location == 'North':
            pass
        elif current_location == 'West':
            pass
        elif current_location == 'East':
            pass
        return WalkChoice()
    elif choice == 3:
        manage_inventory()
    elif choice == 4:
        Ending()
    else:
        print("Invalid direction. Please try again.")
        time.sleep(1)
        return WalkChoice()

def South_Event():
    pass
def North_Event():
    pass
def West_Event():
    pass
def East_event():
    pass


print('-'*30)
print(Style.BRIGHT + Fore.RED + 'Welcome to Dungeon Typing Delight!'+ Style.RESET_ALL)
print('-'*30)
main()