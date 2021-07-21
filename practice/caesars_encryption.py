import string

print('Caesar\'s Crypt')

# def encrypt(operation, word, shift):
#     encoded_word = ''
#     for index in range(len(word)):
#         char = word[index]
#         alphabet_index = alphabet.index(char)
#         if operation == 'encode':
#             new_index = alphabet_index + (shift % len(alphabet))
#             encoded_word += alphabet[new_index]
#         else:
#             new_index = alphabet_index - (shift % len(alphabet))
#             encoded_word += alphabet[new_index]
#     return encoded_word


# REFACTORED IMPLEMENTATION
def encrypt(operation, word, shift):
    encoded_word = ''
    shift = shift % len(alphabet)
    if operation == 'decode':
        shift *= -1
    for char in word:
        alphabet_index = alphabet.index(char)
        new_index = alphabet_index + shift
        encoded_word += alphabet[new_index]
    return encoded_word

alphabet = string.ascii_lowercase
session_over = False

while not session_over:
    operation = input('What operation do you want to perform? Type 0 for encoding, 1 for decoding\n')
    if operation == "0":
        operation = 'encode'
    else:
        operation = 'decode'
    word = input(f'Type what you want to {operation}.\n').lower()
    shift = int(input('How many letters do you want to shift?\n'))

    print(encrypt(operation, word, shift))

    quit = input('Do you want to perform another operation? Y or N\n').lower()
    if quit == 'n':
        session_over = True
