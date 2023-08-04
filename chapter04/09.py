# Problem: Write program to generate all the binary strings of n bits

# A function that generates all k-ary strings
def gen_kary_str(n, k, l = [], idx = 0):
    if idx == n:
        print(*l, sep=' ')
        return
    
    for i in range(k):
        l.append(i)
        gen_kary_str(n, k, l, idx + 1)
        l.pop()

# Enter input
n = int(input('Enter n: '))
k = int(input('Enter k: '))

# Print output
gen_kary_str(n, k)