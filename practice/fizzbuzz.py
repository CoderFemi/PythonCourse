
for num in range(1, 101):
    divisible_by_3 = num % 3 == 0
    divisible_by_5 = num % 5 == 0
    if divisible_by_3 and divisible_by_5:
        print('fizzbuzz')
    elif divisible_by_3:
        print('fizz')
    elif divisible_by_5:
        print('buzz')
    else:
        print(num)