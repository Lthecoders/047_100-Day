import os

os.system('clear')

# Poke_game = {}

# pokemon_1 = 'Charizard'
# pokemon_2 = 'Blastoise'
# pokemon_3 = 'Venusaur'

# Poke_game[pokemon_1] = {
#     'Key attacks': 'fire wing, burning tail',
#     'fire wing': 30,
#     'burning Tail': 80
# }

# Poke_game[pokemon_2] = {
#     'Key attacks': 'Rapid spin, Splash Bomb',
#     'rapid spin': 30,
#     'Splash bomb': 120
# }

# Poke_game[pokemon_3] = {
#     'Key attacks': 'Poison powder, Jungle Hammer',
#     'Poison powder': 60,
#     'Jungle Hammer': 90
# }

# print(list(Poke_game.keys())[2])
# # this is the way to access the key from the 2D dictionery
# """
# first we have to convert our 2d dict to list and then
# we have to access the keys in 2d dict by using key function
# and last becuase now our dict is a list we have to metiond the index

# thus we should be the key name of dict inside a dict"""

import os
import random
import time

print("\n---> 👾 Welcome to the Top Trumps 'Pokemon Battle' simulator. 👾 <----")
print('-----------------------------------------------------\n')

Poke_game = {}

pokemon_0 = 'Charizard'
pokemon_1 = 'Blastoise'
pokemon_2 = 'Venusaur'

Poke_game[pokemon_0] = {
    'Key attacke': 'fire waing, burning tail',
    '1. fire wing': 30,
    '2. burning Tail': 80
}

Poke_game[pokemon_1] = {
    'Key attacke': 'Rapid spin, Splash Bomb',
    '1. rapid spin': 30,
    '2. Splash bomb': 120
}

Poke_game[pokemon_2] = {
    'Key attacke': 'Poison powder, Jungle Hammer',
    '1. Poison powder': 60,
    '2. Jungle Hammer': 90
}

# # print(Poke_game)
# while True:
#   user_pick = input("""
#   0. Charizard
#   1. Blastoise
#   2. Venusaur\n
#   pick your pokemon by side number ---> """).strip()
#   if user_pick == '0':
#     print(f'\n\nyou had choose {list(Poke_game.keys())[0]}\n')
#   elif user_pick == '1':
#     print(f'\n\nyou had choose {list(Poke_game.keys())[1]}')
#   elif user_pick == '2':
#     print(f'\n\nyou had choose {list(Poke_game.keys())[2]}')
#   else:
#     print('\n\ninvalid input, 😨 try to run again choose between 0 to 2')

#   # print(f"You had cossed {user_pick}")
#   print()
#   print()
#   coumputer_pick = random.randint(0, 2)
#   if coumputer_pick == 0:
#     print(f'computer has choose {list(Poke_game.keys())[0]}')
#   elif coumputer_pick == 1:
#     print(f'computer has choose {list(Poke_game.keys())[1]}')
#   elif coumputer_pick == 2:
#     print(f'computer has choose {list(Poke_game.keys())[2]}')

#   #----------> user stats

#   break

for key, value in Poke_game[pokemon_0].items():
    print(f'{key}: {value}')