text = input('Please write a number: ')

if text == text[::-1]:
    print(f'{text} is a Palindrome ')
else:
    print(f'{text} is not a Palindrome ')