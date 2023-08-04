# Problem: Write algorithm that prints all numbers that are smaller than n and are divisible by 3 and 7

# Enter input
n = int(input('Enter n: '))

# Print output
print(f'All numbers that are smaller than {n} and are divisible by 3 and 7: ', end='')
for i in range(7, n, 7):
    if i % 3 == 0:
        print(i, end=' ')