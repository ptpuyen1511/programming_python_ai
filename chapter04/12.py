# Problem: Write program to generate all permutations of k digits

# A function that generates all permutations of k digits
def gen_permutation_len_k(arr, k, li = []):
    global mark
    if len(li) == k:
        print(*li, sep=' ')
        return
    
    for i, e in enumerate(arr):
        if mark[i] == 0:
            mark[i] = 1
            gen_permutation_len_k(arr, k, li + [e])
            mark[i] = 0
    

# Enter input
arr = list(input('Enter n elements/digits (not separated): '))
mark = [0]*len(arr)

# Print output
gen_permutation_len_k(arr, 2)