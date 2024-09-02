import colorama, random
from colorama import*

Docs = ['Item Rarity is defined by it color,' 'Yellow to most powerful items.', 'Blue to items strongs', 'Green to good items.', 'If the item has not color, you should find a better one...',
        'South to battle.', 'East to market.', 'Enemies will return stronger than before. You should prepare.',
        ]

weaponmelee = {
    'knife': {'dano': 5},
    Fore.BLUE + 'sword' + Style.RESET_ALL: {'dano': 10},
    Fore.YELLOW + 'broadsword' + Style.RESET_ALL: {'dano': 15},
    Fore.GREEN + 'shortsword' + Style.RESET_ALL: {'dano': 8},
    'dagger': {'dano': 4},
    'pocket knife': {'dano': 3},
    'brass knuckles': {'dano': 6},
    'baseball bat': {'dano': 7},
    'golf bat': {'dano': 6},
    Fore.BLUE + 'spear' + Style.RESET_ALL: {'dano': 12},
    Fore.BLUE + 'saber' + Style.RESET_ALL: {'dano': 11},
    'scissors': {'dano': 5},
    Fore.YELLOW + 'katana' + Style.RESET_ALL: {'dano': 14},
    'screwdriver': {'dano': 4},
    Fore.GREEN + 'machete' + Style.RESET_ALL: {'dano': 9},
    Fore.BLUE + 'mace' + Style.RESET_ALL: {'dano': 13},
    'chain': {'dano': 7},
    Fore.GREEN + 'sickle' + Style.RESET_ALL: {'dano': 8},
        Fore.GREEN + 'rapier' + Style.RESET_ALL: {'dano': 10},
    Fore.BLUE + 'greatsword' + Style.RESET_ALL: {'dano': 16},
    'club': {'dano': 8},
    Fore.YELLOW + 'scimitar' + Style.RESET_ALL: {'dano': 12},
    'hatchet': {'dano': 6},
    Fore.GREEN + 'pickaxe' + Style.RESET_ALL: {'dano': 9},
    'whip': {'dano': 5},
    Fore.BLUE + 'warhammer' + Style.RESET_ALL: {'dano': 14},
    'cudgel': {'dano': 7},
    Fore.YELLOW + 'battle-axe' + Style.RESET_ALL: {'dano': 15},
    'flail': {'dano': 8},
    Fore.GREEN + 'mallet' + Style.RESET_ALL: {'dano': 10},
    'sickle-sword' + Style.RESET_ALL: {'dano': 11},
        Fore.GREEN + 'falchion' + Style.RESET_ALL: {'dano': 11},
    'billhook': {'dano': 9},
    Fore.BLUE + 'halberd' + Style.RESET_ALL: {'dano': 13},
    'glaive': {'dano': 10},
    Fore.YELLOW + 'claymore' + Style.RESET_ALL: {'dano': 17},
    'partisan': {'dano': 12},
    Fore.GREEN + 'estoc' + Style.RESET_ALL: {'dano': 9},
    'main-gauche': {'dano': 8},
    Fore.BLUE + 'bastard sword' + Style.RESET_ALL: {'dano': 14},
    'war scythe': {'dano': 11},
    Fore.YELLOW + ' executioner\'s sword' + Style.RESET_ALL: {'dano': 18},
    'flamberge': {'dano': 13},
    Fore.GREEN + 'hand axe' + Style.RESET_ALL: {'dano': 7},
    'morning star': {'dano': 10},
}

moves = ['Walking...', 'Climbing...', 'Sneaking...', 'Turning around...',
          'Crawling...', 'Rising...', 'Jumping...', 'Running...', 
          'Trotting...', 'Jumping a hole...', 'Making peristaltic movements...',
]



initialmove = Fore.YELLOW + 'Entering the cave...' + Style.RESET_ALL

walkinfo = [
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
]

inventory = []

Notes = []

current_location = 'Initial'

follow = ['North', 'South', 'East', 'West']

chest_event = False

player_pv = 100
player_pe = 50

player_gold = 0

enemy_str = 50
enemy_pv = random.randint(25,50)
enemy_pe = random.randint(10,25)