def factorial(num):
    if num < 0:
        return 'not valid'
    elif num == 0:
        return 1
    else:
        return (num * factorial(num-1))

num= int(input(f'Enter a number: '))
print(f'Factorial of {num} is: {factorial(num)}')