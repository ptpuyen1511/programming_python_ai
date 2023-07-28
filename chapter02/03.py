# Problem: Write algorithm that finds least common multiple of two number

# A function that finds great common divisor
def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    
    while b != 0:
        (a, b) = (b, a % b)

    return a

# A function that finds least common multiple
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Enter input
a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))

# Print output
print(f'lcm({a}, {b}) = ', lcm(a, b))