number_one = int(input('1st number: '))
number_two = int(input('2nd number: '))
number_three = int(input('3rd number: '))

if number_one > number_two and number_one > number_three:
    print(f'Number {number_one} is the Highest')
elif number_two > number_one and number_two > number_three:
    print(f'Number {number_two} is the Highest')
else:
    print(f'Number {number_three} is the Highest')