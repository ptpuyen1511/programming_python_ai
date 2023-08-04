# Problem: Write algorithm that prints all multiples of x that are smaller than n

# Enter input
x = int(input('Enter x: '))
n = int(input('Enter n: '))

# Print output
print(f'All multiples of {x} that are smaller than {n}: ', end='')
for i in range(x, n):
    if i % x == 0:
        print(i, end=' ')