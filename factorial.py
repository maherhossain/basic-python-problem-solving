number = int(input('Input the Number: '))

factorial = 1

if number == 0:
    print(f'Factorial of {number}! = 1')
else:
    for i in range(1, number+1):
        factorial = factorial*i
    print(f"Factorial of {number}! = {factorial}")