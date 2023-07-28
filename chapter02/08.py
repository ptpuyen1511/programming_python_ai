# Problem: Write algorithm that calculates the sum of the reverses of the first n integers.

# A function that reverses a number using while loop to get each of digit in that number
def reverse(n):
    m = 0

    while (n != 0):
        m = m * 10 + n % 10
        n //= 10

    return m

# Enter input
n = int(input('Enter a positive integer: '))

sum = 0
for i in range(1, n + 1):
    sum += reverse(i)

# Print output
print(f'The sum of the reverses of the first {n} integers: ', sum)