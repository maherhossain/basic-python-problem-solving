number = int(input('Input the Number: '))

prime = False

if number < 1:
    print('A prime number is a whole number greater than 1')
elif number == 1:
    print(f'{number} is not a Prime Number')
else:
    for i in range(2, number):
        if number%i == 0:
            prime = True
            break
    if prime:
        print(f'{number} is not a Prime Number')
    else:
        print(f'{number} is a Prime Number')