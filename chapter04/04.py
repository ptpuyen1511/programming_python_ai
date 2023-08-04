# Problem: Write program to find sum, min, max of a list

# A function that calculates the sum of a list
def calc_sum_recursion(l):
    if len(l) == 1:
        return l[0]

    return l[0] + calc_sum_recursion(l[1:])

# A function that finds the max of a list
def find_max_recursion(l):
    if len(l) == 1:
        return l[0]
    
    return max(l[0], find_max_recursion(l[1:]))

# A function that finds the min of a list
def find_min_recursion(l):
    if len(l) == 1:
        return l[0]
    
    return min(l[0], find_min_recursion(l[1:]))

# Enter input
l_inp = input('Enter a list of number (each number is separated by a space): ')
l = [float(e) for e in l_inp.strip().split()]

# Print output
print('Sum:', calc_sum_recursion(l))
print('Max:', find_max_recursion(l))
print('Min:', find_min_recursion(l))