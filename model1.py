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
def poke_battle(user_attact, coumputer_attact,computer_pokemon,user_pokemon):
  if user_attact > coumputer_attact:
    print(f"{computer_pokemon} cannot fight anymore finally user's {user_pokemon} win 🥳🥳")
    print('that was a great battle 🔥🥵')
  elif coumputer_attact > user_attact:
    print(f'computer had lost the battle with {coumputer_attact} attack')

# print(Poke_game)
while True:
  user_pick = input("""
  0. Charizard
  1. Blastoise
  2. Venusaur\n
  pick your pokemon by side number ---> """).strip()

  if user_pick == '0':
    print(f'\n\nyou had choose {list(Poke_game.keys())[0]}\n')
    global user_pokemon
    user_pokemon = (f'{list(Poke_game.keys())[0]}')  #
    for key, value in Poke_game[pokemon_0].items():
      print(f'{key}')
    chose_attact = input(
        '\nwhich attack you want? choose by number --> ').strip()
    if chose_attact == '1':
      print('You had choose fire wing as attack')
      global user_attact
      user_attact = Poke_game[pokemon_0]['1. fire wing']
    elif chose_attact == '2':
      print('You had choose burning tail as attack')
      user_attact = Poke_game[pokemon_0]['2. burning Tail']
    else:
      print('invalid input, 😨 try to run again choose between 1 to 2')

  elif user_pick == '1':
    print(f'\n\nyou had choose {list(Poke_game.keys())[1]}')
    for key, value in Poke_game[pokemon_1].items():
      print(f'{key}')
      chose_attact = input(
          'which attack you want? choose by number --> ').strip()
      if chose_attact == '1':
        print('You had choose rapid spin as attack')
        user_attact = Poke_game[pokemon_1]['1. rapid spin']
      elif chose_attact == '2':
        print('You had choose Splash bomb as attack')
        user_attact = Poke_game[pokemon_1]['2. Splash bomb']
      else:
        print('invalid input, 😨 try to run again choose between 1 to 2')

  elif user_pick == '2':
    print(f'\n\nyou had choose {list(Poke_game.keys())[2]}')
    for key, value in Poke_game[pokemon_2].items():
      print(f'{key}')
      chose_attact = input(
          'which attack you want? choose by number --> ').strip()
      if chose_attact == '1':
        print('You had choose Poison powder as attack')
        user_attact = Poke_game[pokemon_2]['1. Poison powder']
      elif chose_attact == '2':
        print('You had choose Jungle Hammer as attack')
        user_attact = Poke_game[pokemon_2]['2. Jungle Hammer']
      else:
        print('invalid input, 😨 try to run again choose between 1 to 2')

  else:
    print('\n\ninvalid input, 😨 try to run again choose between 0 to 2')

  # print(f"You had cossed {user_pick}")
  print()
  print()
  coumputer_pick = random.randint(0, 2)
  if coumputer_pick == 0:
    print(f'computer has choose {list(Poke_game.keys())[0]}')
    computer_pokemon = (f'{list(Poke_game.keys())[0]}')
    for key, value in Poke_game[pokemon_0].items():
      print(f'{key}')
      choose_attact = random.randint(1, 2)
      if choose_attact == 1:
        print('computer has choose fire wing as attack')
        coumputer_attact = Poke_game[pokemon_0]['1. fire wing']
      elif choose_attact == 2:
        print('computer has choose burning tail as attack')
        coumputer_attact = Poke_game[pokemon_0]['2. burning Tail']

  elif coumputer_pick == 1:
    print(f'computer has choose {list(Poke_game.keys())[1]}')
    computer_pokemon = (f'{list(Poke_game.keys())[1]}')
    for key, value in Poke_game[pokemon_1].items():
      print(f'{key}')
      choose_attact = random.randint(1, 2)
      if choose_attact == 1:
        print('computer has choose rapid spin as attack')
        coumputer_attact = Poke_game[pokemon_1]['1. rapid spin']
      elif choose_attact == 2:
        print('computer has choose Splash bomb as attack')
        coumputer_attact = Poke_game[pokemon_1]['2. Splash bomb']

  elif coumputer_pick == 2:
    print(f'computer has choose {list(Poke_game.keys())[2]}')
    computer_pokemon = (f'{list(Poke_game.keys())[2]}')
    for key, value in Poke_game[pokemon_2].items():
      print(f'{key}')
      choose_attact = random.randint(1, 2)
      if choose_attact == 1:
        print('computer has choose Poison powder as attack')
        coumputer_attact = Poke_game[pokemon_2]['1. Poison powder']
      elif choose_attact == 2:
        print('computer has choose Jungle Hamer as attack')
        coumputer_attact = Poke_game[pokemon_2]['2. Jungle Hammer']

  #----------> user stats

  poke_battle(user_attact, coumputer_attact, computer_pokemon, user_pokemon)
  break


