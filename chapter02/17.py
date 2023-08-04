# Problem: Write algorithm that calculates S = 1^2 + 2^2 + ... + n^2

# Enter input
n = int(input('Enter a positive number: '))

S = 0
for i in range(1, n + 1):
    S += i**2

# Print output
print(f'1^2 + 2^2 + ... + {n}^2 = {S}')