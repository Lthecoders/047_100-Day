import os
import random
import time

green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
normal = '\033[0m'

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


def poke_battle(user_attact, coumputer_attact, computer_pokemon, user_pokemon,
                gaming_name):
  if user_attact > coumputer_attact:
    print(
        green,
        f"\n\ncomputer's {computer_pokemon} cannot fight anymore finally {gaming_name}'s {user_pokemon} win 🥳🥳",
        normal)
    print('that was a great battle 🔥🥵')
  elif coumputer_attact > user_attact:
    print(
        red,
        f"\n\'{gaming_name}'s {user_pokemon} cannot fight anymore finally computer's {computer_pokemon} win 😔🥺",
        normal)
    print(green, '\n\nBetter luck in next Match 👍👍😉', normal)
  elif user_attact == coumputer_attact:
    print(
        cyan,
        "\n\nWow we have a tie here!!! 🥵🥵 What a great match we saw right now\n\n Both player's Pokemon played well 🤯🤯🤯",
        normal)
    print(
        cyan,
        "\n\nbut both the pokemons cannot fight now, as a resut no one is winner so far.",
        normal)
  else:
    print(
        red,
        '\n🫤🫤🫤🫤 error in poke_game subrutine (in terms of variable possiblities)',
        normal)


print(yellow)
gaming_name = input(
    "\n\nEnter your POKE WORLD's Character name ---> ").strip().upper()
print(normal)
time.sleep(1)
print(f'\n\n\n\n{gaming_name} welcome to the POKE WORLD 👋�')
print('\n\n\ngettig you in the battle with a Pokemon Master!!! 🤩🤯🤯')
print('\n\nLoading the match.....')
print('please wait...')
time.sleep(9)
os.system('clear')

print("\n---> 👾 Welcome to the Top Trumps 'Pokemon Battle' simulator. 👾 <----")
print('-----------------------------------------------------\n')
# print(Poke_game)

while True:
  user_pick = input(f"""
  0. Charizard
  1. Blastoise
  2. Venusaur\n
  {gaming_name} choose your pokemon by side number ---> """).strip()

  if user_pick == '0':
    print(f'\n\nyou had choose {list(Poke_game.keys())[0]} 🔥\n')
    print()
    user_pokemon = (f'{list(Poke_game.keys())[0]}')  #
    for key, value in Poke_game[pokemon_0].items():
      print(f'{key}')
    chose_attact = input(
        '\n\nwhich attack you want? choose by number --> ').strip()
    if chose_attact == '1':
      print('You had choose fire wing as attack')
      user_attact = Poke_game[pokemon_0]['1. fire wing']
    elif chose_attact == '2':
      print('You had choose burning tail as attack')
      user_attact = Poke_game[pokemon_0]['2. burning Tail']
    else:
      print('invalid input, 😨 try to run again choose between 1 to 2')

  elif user_pick == '1':
    print(f'\n\nyou had choose {list(Poke_game.keys())[1]} 💦')
    print()
    user_pokemon = (f'{list(Poke_game.keys())[1]}')
    for key, value in Poke_game[pokemon_1].items():
      print(f'{key}')
    chose_attact = input(
        '\n\nwhich attack you want? choose by number --> ').strip()
    if chose_attact == '1':
      print('You had choose rapid spin as attack')
      user_attact = Poke_game[pokemon_1]['1. rapid spin']
    elif chose_attact == '2':
      print('You had choose Splash bomb as attack')
      user_attact = Poke_game[pokemon_1]['2. Splash bomb']
    else:
      print('invalid input, 😨 try to run again choose between 1 to 2')

  elif user_pick == '2':
    print(f'\n\nyou had choose {list(Poke_game.keys())[2]} 🌿')
    print()
    user_pokemon = (f'{list(Poke_game.keys())[2]}')
    for key, value in Poke_game[pokemon_2].items():
      print(f'{key}')
    chose_attact = input(
        '\n\nwhich attack you want? choose by number --> ').strip()
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
    print(f'computer has choose {list(Poke_game.keys())[0]} 🔥')
    print()
    computer_pokemon = (f'{list(Poke_game.keys())[0]}')
    for key, value in Poke_game[pokemon_0].items():
      print(f'{key}')
    choose_attact = random.randint(1, 2)
    if choose_attact == 1:
      print()
      print('computer has choose fire wing as attack')
      coumputer_attact = Poke_game[pokemon_0]['1. fire wing']
    elif choose_attact == 2:
      print()
      print('computer has choose burning tail as attack')
      coumputer_attact = Poke_game[pokemon_0]['2. burning Tail']

  elif coumputer_pick == 1:
    print(f'computer has choose {list(Poke_game.keys())[1]} 💦')
    print()
    computer_pokemon = (f'{list(Poke_game.keys())[1]}')
    for key, value in Poke_game[pokemon_1].items():
      print(f'{key}')
    choose_attact = random.randint(1, 2)
    if choose_attact == 1:
      print()
      print('computer has choose rapid spin as attack')
      coumputer_attact = Poke_game[pokemon_1]['1. rapid spin']
    elif choose_attact == 2:
      print()
      print('computer has choose Splash bomb as attack')
      coumputer_attact = Poke_game[pokemon_1]['2. Splash bomb']

  elif coumputer_pick == 2:
    print(f'computer has choose {list(Poke_game.keys())[2]} 🌿')
    print()
    computer_pokemon = (f'{list(Poke_game.keys())[2]}')
    for key, value in Poke_game[pokemon_2].items():
      print(f'{key}')
    choose_attact = random.randint(1, 2)
    if choose_attact == 1:
      print()
      print('computer has choose Poison powder as attack')
      coumputer_attact = Poke_game[pokemon_2]['1. Poison powder']
    elif choose_attact == 2:
      print()
      print('computer has choose Jungle Hamer as attack')
      coumputer_attact = Poke_game[pokemon_2]['2. Jungle Hammer']

  #----------> user stats

  poke_battle(user_attact, coumputer_attact, computer_pokemon, user_pokemon,
              gaming_name)
  break
