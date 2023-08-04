# Problem: Write algorithm that calculates the sum of squares of even numbers from 1 to n

# Enter input
n = int(input('Enter a positive integer: '))

sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i**2

# Print output
print(f'The sum of the squares of even numbers from 1 to {n}: ', sum)