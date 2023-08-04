# Problem: Write algorithm that finds least common multiple of two number

# A function that finds great common divisor (recursion)
def gcd_recursion(a, b):
    if a == 0 or b == 0:
        return a + b
    
    return gcd_recursion(b, a % b)

# A function that finds least common multiple
def lcm(a, b):
    return abs(a * b) // gcd_recursion(a, b)

# Enter input
a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))

# Print output
print(f'lcm({a}, {b}) = ', lcm(a, b))