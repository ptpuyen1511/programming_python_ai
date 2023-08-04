# Problem: Write program to find index of x in a decreasing list

# A function that finds index of x in a decreasing list
def binary_search_recursion(l, key, start_idx, end_idx):
    if start_idx <= end_idx:
        middle = int((start_idx + end_idx) / 2)
        if l[middle] == key:
            return middle
        elif key > l[middle]:
            return binary_search_recursion(l, key, start_idx, middle - 1)
        else:
            return binary_search_recursion(l, key, middle + 1, end_idx)
    
    return -1

# Enter input
l_inp = input('Enter a decreasing list (each number is separated by a space): ')
x = float(input('Enter x: '))

l = [float(e) for e in l_inp.strip().split()]

# Print output
print(f'Index of {x} in the list:', binary_search_recursion(l, x, 0, len(l) - 1))