# Problem: Write algorithm that reverses a number

# A function that reverses a number using while loop to get each of digit in that number
def reverse_1(n):
    m = 0

    while (n != 0):
        m = m * 10 + n % 10
        n //= 10

    return m

# A function that reverses a number by convert it to string and reverse string by slicing
def reverse_2(n):
    return int(str(n)[::-1])

# Enter input
n = int(input('Enter a positive integer: '))

# Print output
print(f'Reverse {n} (1) -> ', reverse_1(n))
print(f'Reverse {n} (2) -> ', reverse_2(n))