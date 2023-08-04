# Problem: Write algorithm that calculates the sum of the squares of the first n numbers

s = 0

# Enter input
n = int(input('Enter a positive integer: '))

# Calc sum
for i in range(1, n + 1):
    s += i ** 2

# Print output
print(f'1^2 + 2^2 + ... + {n}^2 = ', s)