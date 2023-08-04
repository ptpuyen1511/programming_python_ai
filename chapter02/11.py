# Problem: Write algorithm that calculates the factorial of n

# Enter input
n = int(input('Enter a positive number: '))

fac = 1
for i in range(1, n + 1):
    fac *= i

# Print output
print(f'{n}! = ', fac)