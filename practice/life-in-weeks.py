print('Average life expectancy is 90 years.')
age = input('What is your age?\n')
years_left = 90 - int(age)
months_left = years_left * 24
weeks_left = years_left * 52
days_left = years_left * 365
print(f'You have {days_left} days, {weeks_left} weeks and {months_left} months left.')