# Algorithm: Write an algorithm that inputs an integer and then returns an integer with digits in reverse order.

# Method 1: Use instruction
def reverse_1(n):
    neg = n < 0
    if neg:
        n *= -1

    res = 0
    while n != 0:
        res = res*10 + n % 10
        n //= 10

    if neg:
        res *= -1

    return res

# Method 2: Convert to string, reverse string, convert back to integer
def reverse_2(n):
    neg = n < 0
    if neg:
        n *= -1

    res = int(''.join(list(str(n))[::-1]))

    if neg:
        res *= -1

    return res

# Enter input
n = int(input('Enter an integer: '))

# Print output
print(f'{n} -> reversed (1) ->', reverse_1(n))
print(f'{n} -> reversed (2) ->', reverse_2(n))