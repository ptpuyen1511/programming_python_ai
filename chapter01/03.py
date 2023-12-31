# Problem: Write an algorithm that inputs a positive integer n, and then outputs that n is a prime number or not

# A function that checks whether a number is prime
def is_prime_number(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1): # n**0.5 is sqrt(n)
        if n % i == 0:
            return False
        
    return True

# Enter input
n = int(input('Enter a positive integer: '))

# Print output
print(f'Is {n} a prime number? -> ', is_prime_number(n))
