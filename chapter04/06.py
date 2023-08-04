# Problem: Write program to find index of x in a list

# A function that finds index of x in a list
def find_x_recursion(l, key, idx=0):
    if len(l) == 0:
        return -1
    
    if l[idx] == key:
        return idx
        
    return find_x_recursion(l, key, idx + 1)

# Enter input
l_inp = input('Enter a list of number (each number is separated by a space): ')
x = float(input('Enter x: '))

l = [float(e) for e in l_inp.strip().split()]

# Print output
print(f'Index of {x} in the list:', find_x_recursion(l, x))