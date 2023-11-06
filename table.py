number = int(input('Please write a number: '))

if number > 0:
    for i in range(1, 11):
        print(f'{number} x {i} = {number*i}')