# Problem: Write algorithm that prints all divisors and analyzes prime factors of an integer

# Enter input
n = int(input('Enter a positive integer: '))

# a. Print all divisors
print(f'All divisors of {n}: 1', end='')
for i in range(2, n + 1):
    if n % i == 0:
        print(f', {i}', end='')

# b. Analyze prime factors
print(f'\n{n} = ', end='')
sqrt_n = int(n**1/2)
for i in range(2, sqrt_n + 1):
    power = 0
    while n % i == 0 and n >= i:
        n //= i
        power += 1
    
    if power:
        print(f'{i}^{power}', end='')
        if n != 1:
            print(' x ', end='')