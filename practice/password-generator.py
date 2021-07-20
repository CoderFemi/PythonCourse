import random
import string

# An alternative approach would be to store the random characters
# in a list, then use the random.shuffle(list) method to randomly shuffle the characters.

print('Welcome to the Password Generator')
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password = ''
total_char = 0

i = 0
while total_char <= 8:
    num_of_letters = int(input('How many letters do you want?\n'))
    num_of_numbers = int(input('How many numbers do you want?\n'))
    num_of_symbols = int(input('How many symbols do you want?\n'))
    total_char = num_of_letters + num_of_numbers + num_of_symbols
    if total_char < 8:
        print('You must have at least eight (8) characters for a secure password!\nHint: letters + numbers + symbols must be greater or equal to 8.\nTry again:\n')
    i += 1

j = 0
while int(len(password)) < total_char:
    rand_list = random.choice([letters, numbers, symbols])
    if rand_list == letters and num_of_letters > 0:
        password += random.choice(letters)
        num_of_letters -= 1
    if rand_list == numbers and num_of_numbers > 0:
        password += random.choice(numbers)
        num_of_numbers -= 1
    if rand_list == symbols and num_of_symbols > 0:
        password += random.choice(symbols)
        num_of_symbols -= 1
    j += 1

print(f'Your password is {password}.')