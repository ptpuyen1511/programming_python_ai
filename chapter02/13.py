# Problem: Write algorithm that checks if a number is prime

# A function that checks if a number is prime
def is_prime_number(n):
    if n < 2:
        return False
    
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
        
    return True

# Enter input
n = int(input('Enter a positive number: '))

# Print output
print(f'Is {n} a prime:', is_prime_number(n))