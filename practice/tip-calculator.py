bill = float(input('Enter bill amount:\n'))
number_of_people = int(input('Enter number of people:\n'))
tip = int(input('What is the percentage tip given?\n'))
bill_with_tip = bill * (1 + int(tip) / 100)
share = bill_with_tip / number_of_people
result = round(share, 2)
print(f'Each person\'s share is ${result}')