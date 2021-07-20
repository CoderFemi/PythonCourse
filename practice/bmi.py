height = input('Please enter your height (m):\n')
weight = input('Please enter your weight (kg):\n')
bmi = float(weight) / float(height)**2
result = round(bmi, 2)
print('You have a BMI of ' + str(result))