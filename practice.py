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
bill = float(input('Enter bill amount:\n'))
number_of_people = int(input('Enter number of people:\n'))
tip = int(input('What is the percentage tip given?\n'))
bill_with_tip = bill * (1 + int(tip) / 100)
share = bill_with_tip / number_of_people
result = round(share, 2)
print(f'Each person\'s share is ${result}')