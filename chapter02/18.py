# Problem: Write algorithm that calculates the sum of the first n integers

# Enter input
n = int(input('Enter a positive number: '))

# Method 1: Use loop 
S1 = 0
for i in range(1, n + 1):
    S1 += i

# Method 1: Use Arithmetic Progression
S2 = (n * (n + 1))/2

# Print output
print(f'Method 1: 1 + 2 + ... + {n} = {S1}')
print(f'Method 2: 1 + 2 + ... + {n} = {S2}')