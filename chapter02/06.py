# Problem: Write algorithm that calculates the sum of the cubics of the first n numbers

s = 0

# Enter input
n = int(input('Enter a postive integer: '))

# Calc sum
for i in range(1, n + 1):
    s += i ** 3

# Print output
print(f'1^3 + 2^3 + ... + {n}^3 = ', s)