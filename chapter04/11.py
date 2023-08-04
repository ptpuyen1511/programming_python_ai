# Problem: Write program to generate all permutations of n digits

# A function that generates all permutations of n digits
def gen_permutation(arr, l, r):
    if l == r:
        print(*arr, sep=' ')
        return
    
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        gen_permutation(arr, l + 1, r)
        arr[l], arr[i] = arr[i], arr[l]

# Enter input
arr = list(input('Enter n elements/digits (not separated): '))

# Print output
gen_permutation(arr, 0, len(arr) - 1)