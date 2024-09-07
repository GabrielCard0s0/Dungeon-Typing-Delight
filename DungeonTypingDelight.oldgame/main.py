import time, sys, random, colorama, lists, os
from listas import weaponmelee, initialmove, moves, inventory, walkinfo, current_location, follow, player_pv, player_pe, enemy_pe, enemy_pv, enemy_str, Notes, Docs, player_gold
from colorama import *

def main():
    time.sleep(1)
    print('-'*30)
    print('Select an option:\n', Fore.GREEN + '1. Start Game\n' + Style.RESET_ALL, Fore.RED + '2. Exit' + Style.RESET_ALL)
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
    time.sleep(1)
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

def Chest_Event_buy():
    time.sleep(2)
    print('-'*30)
    print('You bought a chest!')
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

def add_item_to_inventory(item):
    if len(lists.inventory) < 5:
        lists.inventory.append(item)
        print(f"You added {item} to your inventory.")
    else:
        print("Your inventory is full. You can't carry any more items.")

def remove_item_from_inventory(item):
    if item in lists.inventory:
        lists.inventory.remove(item)
        print(f"You removed {item} from your inventory.")
    else:
        print("You don't have that item in your inventory.")
 
def manage_inventory():
    print("You have the following items in your inventory:")
    for item in inventory:
        print(item)
    return WalkChoice()

def manage_notes():
    print("You have the following docs:")
    for item in Notes:
        print(item)
    return WalkChoice()

def WalkChoice():
    time.sleep(1)
    print('-'*30)
    print(Get_Random_walkinfo())
    print('-'*30)
    time.sleep(1)
    print('You have the following options:')
    print('-'*30)
    print(f'\n1. Current Location\n 2. Follow to...\n 3. inventory\n 4. Status\n 5. Notes\n 6. Exit Game\n')
    choice = int(input('Choose an option: '))
    if choice == 1:
            time.sleep(1)
            print('-'*30)
            print(current_location)
            time.sleep(1)
            return WalkChoice()
    elif choice == 2:
        print('-'*30)
        print(f'1. Go to north\n 2. Go to south\n 3. Go to east\n 4. Go to west(not working yet)')# South sempre == Battle #East sempre == Market #North sempre == descanso
        direction = int(input('Choose a direction: '))
        move_player(direction)
        print('-'*30)
        print(f'You are now in the {current_location}')
        if current_location == 'South':
            time.sleep(2)
            Battle_Enemy()
        elif current_location == 'North':
            Rest_Room()
        elif current_location == 'West':
            pass
        elif current_location == 'East':
            time.sleep(2)
            Shop()
    elif choice == 3:
        manage_inventory()
    elif choice == 4:
        print('-'*30)
        print(f'Your current status: PV {Fore.GREEN}{player_pv}{Style.RESET_ALL}, PE {Fore.YELLOW}{player_pe}{Style.RESET_ALL}')
        print(f'You have {Back.YELLOW}{player_gold}{Style.RESET_ALL} coins.')
        print('-'*30)
        time.sleep(2)
        return WalkChoice()          
    elif choice == 5:
        manage_notes()
    elif choice == 6:
        Ending()
    else:
        print("Invalid direction. Please try again.")
        time.sleep(1)
        return WalkChoice()

def Battle_Enemy():
    global player_pv, player_pe, enemy_pv, enemy_pe, inventory, enemy_str, player_gold
    print('-'*30)
    print(f"You are battling an enemy with {enemy_pv} PV and {enemy_pe} PE!")
    print('-'*30)
    while player_pv > 0 and enemy_pv > 0:
        print(f"Your current PV: {Fore.GREEN}{player_pv}{Style.RESET_ALL}, PE: {Fore.YELLOW}{player_pe}{Style.RESET_ALL}")
        print('-'*30)
        print(f"Enemy's current PV: {Fore.GREEN}{enemy_pv}{Style.RESET_ALL}, PE: {Fore.YELLOW}{enemy_pe}{Style.RESET_ALL}")
        print('-'*30)
        action = input("What do you do? (1) Attack, (2) Defend, (3) Use ability: ")
        print('-'*30)
        if action == "1":
            time.sleep(1)
            print("Choose a weapon to attack with:")
            for i, weapon in enumerate(inventory, 1):
                print(f"{i}. {weapon}")
            weapon_choice = int(input("Enter the number of the weapon: ")) - 1
            chosen_weapon = inventory[weapon_choice]
            damage = weaponmelee[chosen_weapon]['damage']
            enemy_pv -= damage
            print('-'*30)
            print(f"You deal {Fore.RED}{damage}{Style.RESET_ALL} damage to the enemy with your {chosen_weapon}!")
            print('-'*30)
        elif action == "2":
            time.sleep(1)
            # Defesa
            player_pe += 10
            print('-'*30)
            print("You defend and gain 10 PE!")
            print('-'*30)
        elif action == "3":
            time.sleep(1)
            # Habilidade especial
            if player_pe >= 20:
                player_pe -= 20
                damage = random.randint(30, 40)
                enemy_pv -= damage
                print('-'*30)
                print(f"You use a special ability and deal {Fore.RED}{damage}{Style.RESET_ALL} damage to the enemy!")
                print('-'*30)
            else:
                print('-'*30)
                print("You don't have enough PE to use a special ability!")
                print('-'*30)
        else:
            print('-'*30)
            print("Invalid action!")
            print('-'*30)
        if enemy_pv > 0:
            time.sleep(1)
            # Inimigo ataca
            damage = random.randint(10, 20)
            player_pv -= damage
            print(f"The enemy deals {Fore.RED}{damage}{Style.RESET_ALL} damage to you!")
    if player_pv <= 0:
        time.sleep(1)
        print('-'*30)
        print("You died! Game over.")
        print('-'*30)
        Ending()
        print('-'*30)
        time.sleep(1)
        sys.exit(0)
    else:
        time.sleep(1)
        print("You defeated the enemy!")
        enemy_pe = random.randint(15,25)
        enemy_pv = random.randint(25,50)
        enemy_pe += enemy_str
        enemy_pv += enemy_str
        enemy_str += 10
        player_cap = random.randint(1, 100)
        player_gold += player_cap
        print('-'*30)
        print(f'You received {Back.YELLOW}{player_cap}{Style.RESET_ALL} coins. Now you have {Back.YELLOW}{player_gold}{Style.RESET_ALL} coins. ')
        print('-'*30)
        time.sleep(2)
        return Chest_Event()
    
def Rest_Room():
    global player_pv, player_pe, player_gold
    print('-'*30)
    choice = int(input('Do you wanna rest for 25 coins?\n 1. Yes\n 2. Not now\n'))
    if choice == 1:
        if player_gold >= 25:
            player_pe += 50
            player_pv += 50
            player_gold -= 25
            print('-'*30)
            print(f"You rest in the room and recover {Fore.GREEN}{50}{Style.RESET_ALL} of all status points.")
            print(f"PE: {Fore.GREEN}{player_pv}{Style.RESET_ALL}")
            print(f"PV: {Fore.YELLOW}{player_pe}{Style.RESET_ALL}")
        else:
            print('-'*30)
            print("You don't have enough coins to rest.")
            print('-'*30)
            return WalkChoice()
    else:
        print('-'*30)
        print("You choose not to rest.")
        print('-'*30)
        time.sleep(2)
        return WalkChoice()
    time.sleep(1)
    print('-'*30)
    return WalkChoice()
def West_Event():
    pass
def Shop():
    global Notes, Docs, player_gold
    print('-'*30)
    print(f'1. Comprar documentação aleatória (50¢)\n 2. Comprar baú de armas aleatórias(1000¢)\n 3. Voltar')
    print('-'*30)
    action = input("What do you want to do? ")
    if action == '2':
        if player_gold >= 1000:
            time.sleep(2)
            print('-'*30)
            print('You has buy a Doc!')
            print('-'*30)
            time.sleep(2)
            player_gold -= 1000
            docsrandom = random.sample(sorted(Docs), 1)
            print('-'*30)
            print(f'Reading Doc...:{docsrandom}')
            print('-'*30)
            time.sleep(2)        
            Notes.append(docsrandom)
            return WalkChoice()
        else:
            print('-'*30)
            print(f'You dont have enough coins to buy a Doc! You have {Back.YELLOW}{player_gold}{Style.RESET_ALL} coins')
            print('-'*30)
            time.sleep(2)
            return WalkChoice()
    elif action == '1':
        if player_gold >= 50:
            player_gold -= 50
            time.sleep(1)
            return Chest_Event_buy()
        else:
            print('-'*30)
            print(f'You dont have enough coins to buy a Doc! You have {Back.YELLOW}{player_gold}{Style.RESET_ALL} coins')
            print('-'*30)
            time.sleep(2)
            return WalkChoice()
    elif action == '3':
        print('-'*30)
        print("Retornando...")
        print('-'*30)
        time.sleep(1)
        return WalkChoice()
    else:
        print('-'*30)
        print("Invalid action!")
        print('-'*30)
        return WalkChoice()

print('-'*30)
print(Style.BRIGHT + Fore.YELLOW + 'Welcome to Dungeon Typing Delight!'+ Style.RESET_ALL)
print('-'*30)
main()