# Problem: Write algorithm that finds the number of digits in an integer

# A function that finds the number of digits
def findNumDigits(n):
    if n == 0:
        return 1
    
    if n < 0:
        n *= -1

    num_digits = 0
    while n != 0:
        num_digits += 1
        n //= 10

    return num_digits

# Enter input
n = int(input('Enter an integer: '))

# Print output
print(f'{n} has {findNumDigits(n)} digits')