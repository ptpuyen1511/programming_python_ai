# Problem: Write program to calc nCk

# A function that calculate factorial
def calc_fac_recursion(n):
    if n == 0:
        return 1
    return n * calc_fac_recursion(n - 1)

# A function that calculates nCk
def nCk(n, k):
    return calc_fac_recursion(n) / (calc_fac_recursion(k) * calc_fac_recursion(n - k))

# Enter input
n = int(input('Enter n: '))
k = int(input('Enter k: '))

# Print output
print(f'{n}C{k} = {nCk(n, k)}')