import colorama, random
from colorama import*

Docs = ['Item Rarity is defined by it color. \nYellow to most powerful items. \nBlue to items strongs. \nGreen to good items. \nIf the item has not color, you should find a better one...',
        
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

current_location = 'Initial'

follow = ['North', 'South', 'East', 'West']

chest_event = False

player_pv = 100
player_pe = 50

enemy_pv = random.randint(25,50)
enemy_pe = random.randint(10,25)