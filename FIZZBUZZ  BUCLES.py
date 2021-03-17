# Given a list of numbers
# if number is divisible by 3 print Fizz
# if number is divisible by 5 Buzz
# if number is divisible by 3 and 5 print FizzBuzz
# if number is not divisible by 3, or 5, nor 3 and 5, print the number itself.

numbers = [2, 3, 31, 6, 9, 43, 15, 32, 30, 100, 101, 78, 99]
for number in numbers:
    if number % 3 == 0:
        if number % 5 == 0:
            print(f'FizzBuzz {number}')
        else:
            print(f'Fizz {number}')
    elif number % 5 == 0:
        print(f'Buzz {number}')
    else:
        print(f'{number}')
