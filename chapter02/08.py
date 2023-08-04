# Problem: Write algorithm that calculates the sum of the inverses of the first n integers.

# Enter input
n = int(input('Enter a positive integer: '))

sum = 0
for i in range(1, n + 1):
    sum += 1/i

# Print output
print(f'The sum of the reverses of the first {n} integers: ', sum)