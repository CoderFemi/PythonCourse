import random
import os
from hangman_art import stages, logo
from hangman_words import word_list
# from replit import clear

print(logo)


def clear():
    os.system('cls')
    
game_over = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Make a guess: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The word is {chosen_word}")

    if not "_" in display:
        game_over = True
        print("You win!")

    print(stages[lives])
