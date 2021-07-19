#  BMI
# height = input('Please enter your height (m):\n')
# weight = input('Please enter your weight (kg):\n')
# bmi = float(weight) / float(height)**2
# result = round(bmi, 2)
# print('You have a BMI of ' + str(result))


# LIFE-IN-WEEKS
# print('Average life expectancy is 90 years.')
# age = input('What is your age?\n')
# years_left = 90 - int(age)
# months_left = years_left * 24
# weeks_left = years_left * 52
# days_left = years_left * 365
# print(f'You have {days_left} days, {weeks_left} weeks and {months_left} months left.')


# TIP-CALCULATOR
# bill = float(input('Enter bill amount:\n'))
# number_of_people = int(input('Enter number of people:\n'))
# tip = int(input('What is the percentage tip given?\n'))
# bill_with_tip = bill * (1 + int(tip) / 100)
# share = bill_with_tip / number_of_people
# result = round(share, 2)
# print(f'Each person\'s share is ${result}')



# PIZZA-ORDER
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