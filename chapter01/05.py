# A function that calc x^y using fast power algorithm
def fast_power(x, y):
    res = 1
    
    while y > 0:
        if y % 2 == 1:
            res *= x
        
        x *= x
        y //= 2

    return res

# Enter input
x = int(input('Enter x: '))
y = int(input('Enter y: '))

# Print output
print(f'{x}^{y} = ', fast_power(x, y))
