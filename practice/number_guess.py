from random import choice
from logos import guess_logo

print(f'{guess_logo}\nWELCOME TO THE GUESSING GAME!')

def guessing_game():
    lower_range = choice(range(50))
    upper_range = lower_range + 50
    number = choice(range(lower_range, upper_range))
    print(f"I'm thinking of a number between {lower_range} and {upper_range}.")

    difficulty = input('Type 0 for easy and 1 for hard.\n')
    tries = 0
    if difficulty == '0':
        print("You're playing in easy mode:")
        tries = 10
    elif difficulty == '1':
        print("You're playing in hard mode:")
        tries = 5
    else:
        print('You made an invalid selection. The default is easy mode.')
        tries = 10

    print(f'You have {tries} attempts left to guess the number. ')

    while tries > 0:
        user_input = input('Make a guess:\n')
        guess: int = check_input(user_input)
        if guess == number:
            print('You guessed correctly! You won.')
            replay()
            break
        elif guess > number:
            tries -= 1
            print('Your guess is too high.')
            if tries > 0:
                print(f'You have {tries} attempts left. ')
        else:
            tries -= 1
            print('Your guess is too low.')
            if tries > 0:
                print(f'You have {tries} attempts left. ')

        if tries == 0:
            print(f"Sorry, you lost. The mystery number is {number}.")
            replay()      

def replay():
    play_again = input('Do you want to play again? Y or N:\n').lower()
    if play_again == 'y':
        guessing_game()
    else:
        print('GOODBYE!')

def check_input(user_input: str) -> int:
    try:
        valid_guess = int(user_input)
        return valid_guess
    except ValueError:
        guess_again = input('You supplied the wrong type of input. Please type a valid number:\n')
        return check_input(guess_again)
        
guessing_game()