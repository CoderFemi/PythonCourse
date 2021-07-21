bill = 0
print('Welcome to Pizza Place!')
order = input('What size would you like to order:\nSmall: $15, Medium: $20, Large: $25\nPlease type S, M or L\n')
if order == 'S':
    bill = 15
elif order == 'M':
    bill = 20
else:
    bill = 25
wants_topping = input('Would you like some topping? Y or N?\n')
if wants_topping == 'Y':
    topping = input('What topping(s) would you like?\nSmall Pepperoni: $2, Other Pepperoni: $3, Extra Cheese: $1\nPlease type SP, OP or XC\n')
    if topping == 'SP':
        bill += 2
    elif topping == 'OP':
        bill += 3
    else:
        bill += 1

print(f'Your bill is ${bill}.')
