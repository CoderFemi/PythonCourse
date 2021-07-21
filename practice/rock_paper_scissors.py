import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp_win = False
player_win = False

print('Let\'s play rock-paper-scissors!')
comp_choice = random.choice([rock, paper, scissors])
player_choice = int(input('Type 0 for rock, 1 for paper and 2 for scissors.\n'))

i = 0
while player_choice < 0 or player_choice > 2:
    if i > 1:
        print('You have not selected a valid number. Please play again.')
        quit()
    player_choice = int(input('Please type a valid number:\n'))
    i += 1

if player_choice == 0:
    player_choice = rock
elif player_choice == 1:
    player_choice = paper
else:
    player_choice = scissors


if player_choice == rock and comp_choice == paper:
    comp_win = True
elif player_choice == paper and comp_choice == rock:
    player_win = True
elif player_choice == scissors and comp_choice == paper:
    player_win = True
elif player_choice == rock and comp_choice == scissors:
    player_win = True
elif player_choice == paper and comp_choice == scissors:
    comp_win = True
elif player_choice == scissors and comp_choice == rock:
    comp_win = True

print(f'COMPUTER CHOSE:\n{comp_choice}\n\nYOU CHOSE:\n{player_choice}')
if player_win == True:
    print('Congratulations, you won the game!')
elif comp_win == True:
    print('Sorry, you lost the game.')
elif player_win == False and comp_win == False:
    print('There is no winner, you drew the game!')