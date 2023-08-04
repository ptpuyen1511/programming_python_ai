# Problem: Write algorithm that calculates x^n, in which x is a float and n is an integer

# A function that calculates x^n
def power(x, n):
    p = 1
    
    for _ in range(n):
        p *= x

    return p

# Enter input
x = float(input('Enter a float number: '))
n = int(input('Enter a positive number: '))

# Print output
## Our function
print(f'{x}^{n} =', power(x, n))
## Python's function
print(f'{x}^{n} = {x**n}')