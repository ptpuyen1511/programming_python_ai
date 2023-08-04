# Problem: Write program to check if a list is increasing

# A function that checks if a list is increasing
def is_increasing_recursion(l):
    if len(l) < 2:
        return True
    elif len(l) == 2:
        return l[0] <= l[1]
    
    return l[0] <= l[1] and is_increasing_recursion(l[1:])

# Enter input
l_inp = input('Enter a list of number (each number is separated by a space): ')
l = [float(e) for e in l_inp.strip().split()]

# Print output
print('Is this list increasing? ->', is_increasing_recursion(l))