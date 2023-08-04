# Write program to find the nth element of Fibonacci sequence

# A function that return nth element of Fibonacci
def find_n_fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return find_n_fibo(n - 1) + find_n_fibo(n - 2)

# Enter input
n = int(input('Enter n: '))

# Print output
print(f'The {n}th element of Fibonacci is:', find_n_fibo(n))