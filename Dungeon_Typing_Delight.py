import random, colorama, sys, lists, time, wave, pygame
from colorama import *
from pydub import AudioSegment
from pydub.playback import play

class Player:
    def __init__(self, health, energy, gold, rest):
        self.player_health = round(float(health), 2)
        self.player_energy = round(float(energy), 2)
        self.player_gold = round(float(gold), 2)
        self.player_level_rate = 0
        self.player_level = 1


    def Print_Status(self):
        print('-'*50)
        print(f'Your current status: PV {Fore.GREEN}{self.player_health}{Style.RESET_ALL}')
        print(f'Your current status: PE {Fore.YELLOW}{self.player_energy}{Style.RESET_ALL}')
        print(f'You have {Back.YELLOW}{round(self.player_gold, 2)}{Style.RESET_ALL} coins.')
        print(f'You have {round(rest_room.player_rest, 2)} sleep-points.')
        print(f'Your current level is: {self.player_level}')
        print('-'*50)
       
class Player_Inventory:
    def __init__(self):
        self.player_items = {}

    def Print_Inventory(self):
        print('-'*50)
        print('You have the following itens:')
        for i, item in enumerate(self.player_items, 1):
            print(f'{i}. {item} - Damage: {self.player_items[item]["damage"]}')
            time.sleep(1)
        print('-'*50)
    
    def Add_Item(self, item, damage):
        self.player_items.update({item: {'damage': damage}})

    def Remove_Item(self, item):
        if item in self.player_items:
            del self.player_items[item]

class Items_to_Find:
    def __init__(self):
        self.items = {
            'knife': {'damage': 3},
            Fore.BLUE + 'sword' + Style.RESET_ALL: {'damage': 10},
            Fore.YELLOW + 'broadsword' + Style.RESET_ALL: {'damage': 15},
            Fore.GREEN + 'shortsword' + Style.RESET_ALL: {'damage': 8},
            'dagger': {'damage': 4},
            'pocket knife': {'damage': 2},
            'brass knuckles': {'damage': 5},
            'baseball bat': {'damage': 7},
            'golf bat': {'damage': 6},
            Fore.BLUE + 'spear' + Style.RESET_ALL: {'damage': 12},
            Fore.BLUE + 'saber' + Style.RESET_ALL: {'damage': 11},
            'scissors': {'damage': 5},
            Fore.YELLOW + 'katana' + Style.RESET_ALL: {'damage': 14},
            'screwdriver': {'damage': 4},
            Fore.GREEN + 'machete' + Style.RESET_ALL: {'damage': 9},
            Fore.BLUE + 'mace' + Style.RESET_ALL: {'damage': 13},
            'chain': {'damage': 7},
            Fore.GREEN + 'sickle' + Style.RESET_ALL: {'damage': 8},
            Fore.GREEN + 'rapier' + Style.RESET_ALL: {'damage': 10},
            Fore.BLUE + 'greatsword' + Style.RESET_ALL: {'damage': 16},
            'club': {'damage': 8},
            Fore.YELLOW + 'scimitar' + Style.RESET_ALL: {'damage': 12},
            'hatchet': {'damage': 6},
            Fore.GREEN + 'pickaxe' + Style.RESET_ALL: {'damage': 9},
            'whip': {'damage': 5},
            Fore.BLUE + 'warhammer' + Style.RESET_ALL: {'damage': 14},
            'cudgel': {'damage': 7},
            Fore.YELLOW + 'battle-axe' + Style.RESET_ALL: {'damage': 15},
            'flail': {'damage': 8},
            Fore.GREEN + 'mallet' + Style.RESET_ALL: {'damage': 10},
            'sickle-sword' + Style.RESET_ALL: {'damage': 11},
            Fore.GREEN + 'falchion' + Style.RESET_ALL: {'damage': 11},
            'billhook': {'damage': 9},
            Fore.BLUE + 'halberd' + Style.RESET_ALL: {'damage': 13},
            'glaive': {'damage': 10},
            Fore.YELLOW + 'claymore' + Style.RESET_ALL: {'damage': 17},
            'partisan': {'damage': 10},
            Fore.GREEN + 'estoc' + Style.RESET_ALL: {'damage': 9},
            'main-gauche': {'damage': 8},
            Fore.BLUE + 'bastard sword' + Style.RESET_ALL: {'damage': 14},
            'war scythe': {'damage': 10},
            Fore.YELLOW + 'executioner\'s sword' + Style.RESET_ALL: {'damage': 18},
            'flamberge': {'damage': 10},
            Fore.GREEN + 'hand axe' + Style.RESET_ALL: {'damage': 7},
            'morning star': {'damage': 10},
        }

    def Chest_Event(self):
        time.sleep(2)
        print('-'*50)
        print('You found a chest!')
        print('-'*50)
        weapons = random.sample(sorted(self.items), 3)
        sounds.Open_chest()
        print('You found the following items:')
        print('-'*50)
        for i, weapon in enumerate(weapons, 1):
            print(f'{i}. {weapon} - Damage: {self.items[weapon]["damage"]}')
        print('-'*50)
        while True:
            try:
                choice = int(input('Which item do you want to take? > ')) - 1
                break  # sair do loop se tudo foi bem-sucedido
            except (ValueError, TypeError) as e:
                print('Invalid input. Please enter a number.')
                time.sleep(1)
                continue
        chosen_weapon = weapons[choice]
        print('-'*50)
        print(f'You took the {chosen_weapon}')
        print('-'*50)
        time.sleep(1)
        player_inventory.Add_Item(chosen_weapon, self.items[chosen_weapon]["damage"])


class Player_Notes:
    def __init__(self):
        self.notes = []
    
    def Print_Notes(self):
        print(f'Your notes:\n')
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

    def Add_note(self, note):
        self.notes.append(note)

    def Remove_Item(self, note):
        self.notes.remove(note)


class Notes_to_Find:
    def __init__(self):
        self.notes = [
            'Item Rarity is defined by it color',
            'Yellow to most powerful items.',
            'Blue to items strongs', 
            'Green to good items.', 
            'If the item has not color, you should find a better one...',
            'South to battle.',
            'East to market.', 
            'Enemies will return stronger than before. You should prepare.',
            'Keep an eye on your health, it can drop quickly!',
            'Some items have special abilities, use them wisely!',
            'Don\'t forget to rest and recover your energy!',
            'Explore the world, there are many secrets to discover!',
            'Be careful with your gold, you never know when you\'ll need it!',
        ]



class Moves:
    def __init__(self):
        self.move = [
            Fore.YELLOW + 'Entering the world...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the game...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the adventure...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the way...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the certanly death...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the unknown...' + Style.RESET_ALL,
            Fore.YELLOW + 'Entering the depths of the cave...' + Style.RESET_ALL,
        ]
        self.current_location = 'Center'
        self.choice = ['Center', 'North', 'South', 'East', 'West']
        self.walkinfo = [
            'You are walking...',
            'You are walking through the cave.',
            'You take a step forward, the sound echoes off the walls.',
            'Your footsteps are the only sound in the darkness.',
            'You continue on your journey, the cave stretches out before you.',
            'You walk cautiously, the ground beneath your feet is uneven.',
            'You make your way deeper into the cave, the air grows thick.',
            'You walk with purpose, your heart beats with anticipation.',
            'You take a deep breath, the smell of damp earth fills your nostrils.',
            'You move forward, the sound of dripping water grows louder.',
            'You are getting close to something...',
            'You sense a presence around you.',
            'You hear a noise coming from a distance.',
            'You are approaching a fork in the road.',
            'The path ahead of you is shrouded in darkness.',
            'You can feel the weight of the cave bearing down on you.',
            'You are not alone in the cave.',
            'You hear the sound of scurrying rodents.',
            'The air is thick with the smell of mold and decay.',
            'You can see a faint light in the distance.',
            'You are getting closer to the heart of the cave.',
        ]

    def First_Step(self):
        print('-'*50)
        elemento = random.choice(self.move)
        print(elemento)
        print('-'*50)
    
    def Self_Walk_Info(self):
        print('-'*50)
        print(random.choice(self.walkinfo))
        print('-'*50)
    
    def Location_Change(self, choice):
        if choice == 'n':
            self.current_location = self.choice[1]
            moves.Print_Location()
            time.sleep(1)
        elif choice == 's':
            self.current_location = self.choice[2]
            moves.Print_Location()
            time.sleep(1)
        elif choice == 'e':
            self.current_location = self.choice[3]
            moves.Print_Location()
            time.sleep(1)
        elif choice == 'w':
            self.current_location = self.choice[4]
            moves.Print_Location()
            time.sleep(1)
        else:
            print('-'*50)
            print('Invalid choice')
            print('-'*50)
            time.sleep(1)

    def Print_Location(self):
        print('-'*50)
        print(f'You are Here: {self.current_location}')
        print('-'*50)

    def Direction(self):
        time.sleep(1)
        print('-'*50)
        print('Choose your destiny:')
        print('North[N], South[S], East[E], West[W], Exit[X]:')
        try:
            choice = input('> ').lower()
        except ValueError as e:
            print('Invalid choice')
            time.sleep(1)
            self.Direction()
        except TypeError as e:
            print('Invalid choice')
            time.sleep(1)
            self.Direction()
        if choice == 'n':
            moves.Location_Change(choice)
            rest_room.Sleep()
        elif choice == 's':
            moves.Location_Change(choice)
            battle.Battle_Enemy()
        elif choice == 'e':
            moves.Location_Change(choice)
            market.Shop()
        elif choice == 'w':
            moves.Location_Change(choice)
            upgrade.Upgrade_Menu()
        elif choice == 'x':
            game.Game_Over()
        else:
            print('Invalid choice')
            

    def Get_Random_Walk_Info(self):
        return random.choice(self.walkinfo)
             
class Market:
    def __init__(self):
        self.market = 0
    
    def Shop(self):
        print('-'*50)
        moves.Print_Location
        print('-'*50)
        moves.current_location = moves.choice[0]
        time.sleep(1)
        print('-'*50)
        print('Welcome to the Market')
        print('-'*50)
        print(f'You have {round(player.player_gold, 2)} gold')
        print('-'*50)
        time.sleep(1)
        print(f'1. Buy a random Doc (50¢)\n 2. Buy a random chest (1000¢)\n X. go back')
        try:
            action = input('> ').lower()
        except ValueError as e:
            print('Invalid choice')
            time.sleep(1)
            self.Shop()
        except TypeError as e:
            print('Invalid choice')
            time.sleep(1)
            self.Shop()
        while action != 'x':
            if action == '1':
                if player.player_gold >= 50:
                    time.sleep(1)
                    print('-'*50)
                    print('You has buy a Doc!')
                    print('-'*50)
                    player.player_gold -= 50
                    random_note = random.sample(sorted(notes_to_find.notes), 1)
                    player_notes.Add_note(random_note)
                    print('-'*50)
                    print(f'Reading Doc...: {random_note}')
                    print('-'*50)
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    print('-'*50)
                    print("You dont have enough coins to buy a Doc.")
                    print('-'*50)
                    print(f'You have: {player.player_gold}')
                    print('-'*30)
                    time.sleep(1)
            elif action == '2':
                if player.player_gold >= 1000:
                    time.sleep(1)
                    print('-'*50)
                    print('You has buy a chest!')
                    print('-'*50)
                    weapons = random.sample(sorted(items_to_find.items), 1)
                    print('You found the following item:')
                    print('-'*50)
                    for i, weapon in enumerate(weapons, 1):
                        print(f'{i}. {weapon} - Damage: {items_to_find.items[weapon]["damage"]}')
                    print('-'*50)
                    chosen_weapon = weapons[0]
                    print('-'*50)
                    print(f'You took the {chosen_weapon}')
                    print('-'*50)
                    player_inventory.Add_Item(chosen_weapon, items_to_find.items[chosen_weapon]["damage"])
                    time.sleep(1)
            else:
                print('-'*50)
                print('Invalid action')
                print('-'*50)
                time.sleep(1)
        print('-'*50)
        print(f'...Returning')
        print('-'*50)
        time.sleep(1)

class Battle:
    def __init__(self):
        self.enemy_health = round(random.uniform(25,50), 2)
        self.enemy_energy = round(random.uniform(10, 25), 2)
        self.level = float(0)

    def Battle_Enemy(self):
        print('-'*50)
        moves.Print_Location
        print('-'*50)
        moves.current_location = moves.choice[0]
        print('-'*50)
        print(f'You are in a battle with an enemy with PV: {self.enemy_health} and PE: {self.enemy_energy}')
        print('-'*50)
        time.sleep(1)
        while player.player_health > 0 and self.enemy_health > 0:
            time.sleep(1)
            print(f"Your current PV: {Fore.GREEN}{round(player.player_health, 2)}{Style.RESET_ALL}, PE: {Fore.YELLOW}{round(player.player_energy, 2)}{Style.RESET_ALL}")
            print('-'*50)
            print(f"Enemy's current PV: {Fore.GREEN}{round(self.enemy_health, 2)}{Style.RESET_ALL}, PE: {Fore.YELLOW}{round(self.enemy_energy, 2)}{Style.RESET_ALL}")
            print('-'*50)
            print('What do you do? (1) Attack, (2) Defend, (3) Use ability')
            try:
                print('-'*50)
                action = input('> ')
                print('-'*50)
            except ValueError as e:
                print(f'Invalid action: {e}')
                time.sleep(1)
                continue
            except TypeError as e:
                print(f'Invalid action: {e}')
                time.sleep(1)
                continue
            if action == '1':
                time.sleep(1)
                print('Choose a weapon to attack with: ')
                weapons = list(player_inventory.player_items.keys())
                for i, weapon in enumerate(weapons, 1):
                    print(f'{i}. {weapon}')
                try:
                    weapon_choice = int(input('> ')) - 1
                except ValueError as e:
                    print(f'Invalid choice: {e}')
                    time.sleep(1)
                    continue
                except TypeError as e:
                    print(f'Invalid choice: {e}')
                    time.sleep(1)
                    continue
                chosen_weapon = weapons[weapon_choice]
                damage = player_inventory.player_items[chosen_weapon]['damage']
                self.enemy_health -= damage
                print('-'*50)
                sounds.Attack()
                print(f"You hit the enemy for {round(damage, 2)} damage with your {chosen_weapon}.")
                print('-'*50)
                time.sleep(1)
            elif action == '2':
                time.sleep(1)
                player.player_energy += 10
                print('-'*50)
                print(f"You defend and gain 10 PE. Your current PE is {player.player_energy}")
                print('-'*50)
                time.sleep(1)
            elif action == '3':
                time.sleep(1)
                if player.player_energy >= 20:
                    player.player_energy -= 20
                    damage = round(random.uniform(30, 50), 2) + player.player_level_rate
                    self.enemy_health -= damage
                    print('-'*50)

                    print(f"You use your ability and deal {round(damage, 2)} damage to the enemy")
                else:
                    print('-'*50)
                    print("You don't have enough PE to use a special ability!")
                    print('-'*50)
            else:
                print('-'*50)
                print("Invalid action!")
                print('-'*50)
            if self.enemy_health > 0:
                time.sleep(1)
                damage = round(random.uniform(10, 20), 2) + self.level
                player.player_health -= damage
                print(f"The enemy deals {Fore.RED}{damage}{Style.RESET_ALL} damage to you!")

        if player.player_health <= 0:
            time.sleep(1)
            print('-'*50)
            print('You are defeated')
            print('-'*50)
            game.Game_Over()
        
        else:
            time.sleep(1)
            print('-'*50)
            print('You are victorious')
            print('-'*50)
            self.level += 0.50
            player.player_level_rate += 0.01
            if player.player_level_rate >= 0.10:
                player.player_level_rate = 0.01
                player.player_level += 1
                sounds.Level_Up()
                print(f'You advanced to next level: {player.player_level}')
            self.enemy_energy = round(random.uniform(15, 25) + self.level, 2)
            self.enemy_health = round(random.uniform(25, 50) + self.level, 2)
            player_reward = round(random.uniform(1, 100) + player.player_level_rate + player.player_level, 2)
            player.player_gold += round(player_reward, 2)
            rest_points = 0.10
            rest_room.player_rest += round(rest_points)
            print('-'*50)
            print(f'You received {Back.YELLOW}{player_reward}{Style.RESET_ALL} coins. Now you have {Back.YELLOW}{round(player.player_gold, 2)}{Style.RESET_ALL} coins.')
            print('-'*50)
            time.sleep(1)
            items_to_find.Chest_Event()


class Rest_Room:
    def __init__(self):
        self.player_rest = 0
    
    def Sleep(self):
        print('-'*50)
        moves.Print_Location
        print('-'*50)
        moves.current_location = moves.choice[0]
        time.sleep(1)
        print('-'*50)
        print(f'You have {self.player_rest} sleep-points')
        print(''*50)
        if self.player_rest >= 1:
            print(f'You need 1 sleep-point to sleep. Do you wanna use it? [S/N]')
            try:
                action = input('> ').lower()
            except ValueError as e:
                print(f'Invalid input: {e}')
                time.sleep(1)
                self.Sleep()
            except TypeError as e:
                print(f'Invalid input: {e}')
                time.sleep(1)
                self.Sleep()
            while action != 'n':
                if action == 's':
                    self.player_rest -= 1
                    print(f'You rested for 1 night.')
                    time.sleep(1)
                    print('-'*50)
                    print(f'Now, you have {self.player_rest} sleep-points')
                else:
                    time.sleep(1)
                    print('-'*50)
                    print('Invalid input.')
                    print('-'*50)
                    time.sleep(1)
        else:
            time.sleep(1)
            print('-'*50)
            print('You don\'t have enough sleep-points')
            print('-'*50)
            time.sleep(1)
            
            
class Upgrade:
    def __init__(self):
        self.upgrade_options = [
            '1. Upgrade PV (+10 PV)[$50]',
            '2. Upgrade PE (+10 PE)[$50]',
            '3. Upgrade damage (+5 damage)[$200]',
            '4. Upgrade defense (+5 defense)[$200]',
        ]

    def Upgrade_Menu(self):
        print('-'*50)
        moves.Print_Location
        print('-'*50)
        moves.current_location = moves.choice[0]
        time.sleep(1)
        print('-'*50)
        print('You are in Upgrade Menu!')
        print('-'*50)
        for option in self.upgrade_options:
            print(option)
        try:
            choice = int(input('> '))
        except ValueError as e:
            print('-'*50)
            print('Invalid Option! Please, choose a valid option (1-4)')
            print('-'*50)
            time.sleep(1)
            self.Upgrade_Menu()
        except TypeError as e:
            print('-'*50)
            print('Invalid Option! Please, choose a valid option (1-4)')
            print('-'*50)
            time.sleep(1)
            self.Upgrade_Menu()
        if choice == 1:
            self.Upgrade_Health()
        elif choice == 2:
            self.Upgrade_Energy()
        elif choice == 3:
            self.Upgrade_Damage()
        elif choice == 4:
            self.Upgrade_Defense()
        else:
            print('-'*50)
            print('Opção inválida!')
            print('-'*50)
            time.sleep(1)

    def Upgrade_Health(self):
        time.sleep(1)
        if player.player_gold >= 100:
            player.player_health += 10
            player.player_gold -= 100
            print('-'*50)
            print('Você atualizou sua saúde!')
            print('-'*50)
        else:
            time.sleep(1)
            print('-'*50)
            print('Você não tem ouro suficiente!')
            print('-'*50)

    def Upgrade_Energy(self):
        time.sleep(1)
        if player.player_gold >= 100:
            player.player_energy += 10
            player.player_gold -= 100
            print('-'*50)
            print('Você atualizou sua energia!')
            print('-'*50)
        else:
            time.sleep(1)
            print('-'*50)
            print('Você não tem ouro suficiente!')
            print('-'*50)

    def Upgrade_Damage(self):
        time.sleep(1)
        if player.player_gold >= 200:
            player.player_level_rate += 0.05
            player.player_gold -= 200
            print('-'*50)
            print('Você atualizou seu dano!')
            print('-'*50)
        else:
            time.sleep(1)
            print('-'*50)
            print('Você não tem ouro suficiente!')
            print('-'*50)

    def Upgrade_Defense(self):
        time.sleep(1)
        if player.player_gold >= 200:
            player.player_health += 5
            player.player_gold -= 200
            print('-'*50)
            print('Você atualizou sua defesa!')
            print('-'*50)
        else:
            time.sleep(1)
            print('-'*50)
            print('Você não tem ouro suficiente!')
            print('-'*50)

class Sounds():
    def __init__(self):
        pass   
    
    def Play_Intro(self):
        pygame.mixer.music.load('sounds/maintheme.mp3')
        pygame.mixer.music.play(-1)

    def Attack(self):
        attack = pygame.mixer.Sound('sounds/attack.flac')
        pygame.mixer.Sound.play(attack)
    
    def Ability(self):
        ability = pygame.mixer.Sound('sounds/ability.flac')
        pygame.mixer.Sound.play(ability)

    def Level_Up(self):
        level_up = pygame.mixer.Sound('sounds/levelup.mp3')
        pygame.mixer.Sound.play(level_up)

    def Game_Over(self):
        pygame.mixer.music.load('sounds/gameover.mp3')
        pygame.mixer.music.play()
    
    def Open_chest(self):
        open_chest = pygame.mixer.Sound('sounds/openchest.mp3')
        pygame.mixer.Sound.play(open_chest)

class Game:
    def __init__(self):
        self.game_over = False
        self.options = [
        f'{Fore.GREEN}[1]Start Game{Style.RESET_ALL}',
        f'{Fore.RED}[2]Exit{Style.RESET_ALL}',
        ]
        self.selections = [
        '1. Current Location',
        '2. Follow to...',
        '3. inventory',
        '4. Status',
        '5. Notes',
        '6. Exit Game',
        ]
        self.choice = 0

    def Gaming(self):
        print('-'*50)
        print(Style.BRIGHT + Fore.YELLOW + 'Welcome to Dungeon Typing Delight!'+ Style.RESET_ALL)
        print('-'*50)
        sounds.Play_Intro()
        time.sleep(1)
        self.Options()
        items_to_find.Chest_Event()
        while self.game_over != True:
            moves.Self_Walk_Info()
            time.sleep(1)

            moves.Print_Location()    
            time.sleep(1)

            print('-'*50)
            self.Selection()
            print('-'*50)

        sys.exit(0)
    def Options(self):
        for option in self.options:
            print(f'{option}')
        try:
            self.choice = int(input('> '))
        except ValueError as e:
            print(f'{Fore.RED}Invalid Input! Try again.{Style.RESET_ALL}')
            time.sleep(1)
            self.Options()
        except TypeError as e:
            print(f'{Fore.RED}Invalid Input! Try again.{Style.RESET_ALL}')
            time.sleep(1)
            self.Options()
        self.Selectoption()
    
    def Selectoption(self):
        if self.choice == 1:
            return moves.First_Step()
        elif self.choice == 2:
            return self.Game_Over()

    def Selection(self):
        for selection in self.selections:
            print(f'{selection}')
        try:
            choice = int(input('> '))
        except ValueError as e:
            print(f'{Fore.RED}Invalid Input! Try again.{Style.RESET_ALL}')
            time.sleep(1)
            self.Selection()
        except TypeError as e:
            print(f'{Fore.RED}Invalid Input! Try again.{Style.RESET_ALL}')
            time.sleep(1)
            self.Selection()
        if choice == 1:
            moves.Print_Location()
        elif choice == 2:
            moves.Direction()
        elif choice == 3:
            player_inventory.Print_Inventory()
        elif choice == 4:
            player.Print_Status()
        elif choice == 5:
            player_notes.Print_Notes()
        elif choice == 6:
            game.Game_Over()
        else:
            print("Invalid direction. Please try again.")
            time.sleep(1)
            return game.Selection()

    def Game_Over(self):
        print('-'*50)
        print(f"Finalizando...")
        print('-'*50)
        sounds.Game_Over()
        time.sleep(5)
        self.game_over = True



player = Player(100, 50, 0, 0)
player_inventory = Player_Inventory()
items_to_find = Items_to_Find()
notes_to_find = Notes_to_Find()
player_notes = Player_Notes()
rest_room = Rest_Room()
moves = Moves()
game = Game()
battle = Battle()
market = Market()
upgrade = Upgrade()
sounds= Sounds()

pygame.init()




game.Gaming()