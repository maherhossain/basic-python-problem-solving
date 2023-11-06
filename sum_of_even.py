number = int(input('Please write a number: '))

sum = 0

while number > 1:
    if number % 2 == 0:
        sum += number
    number-=1
print(f'Sum of even number = {sum}')