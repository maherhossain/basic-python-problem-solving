number = int(input('Please write a number: '))

num_one = 0
num_two = 1

print(num_one, num_two, end=" ")
for i in range(2, number+1):
    num_three = num_one + num_two
    num_one = num_two
    num_two = num_three
    print(num_three, end=" ")