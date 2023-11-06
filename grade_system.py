
number = int(input('Input the Number: '))

if number>100 or number<0:
    print('Invalid Number! Please enter between 0 to 100')
elif number >= 90:
    print(f'{number} is "A" Grade, Grade Point 4.00')
elif 86 <= number < 90:
    print(f'{number} is "A-" Grade, Grade Point 3.67')
elif 82 <= number < 86:
    print(f'{number} is "B+" Grade, Grade Point 3.33')
elif 78 <= number < 82:
    print(f'{number} is "B" Grade, Grade Point 3.00')
elif 74 <= number < 78:
    print(f'{number} is "B-" Grade, Grade Point 2.67')
elif 70 <= number < 74:
    print(f'{number} is "C+" Grade, Grade Point 2.33')
elif 66 <= number < 70:
    print(f'{number} is "C" Grade, Grade Point 2.00')
elif 62 <= number < 66:
    print(f'{number} is "C-" Grade, Grade Point 1.67')
elif 58 <= number < 62:
    print(f'{number} is "D+" Grade, Grade Point 1.33')
elif 55 <= number < 58:
    print(f'{number} is "D" Grade, Grade Point 1.00')
else:
    print(f'{number} is "F" Grade, Grade Point 0.00')