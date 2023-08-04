# Problem: Write program to generate print all sub-arrays that have sum equal to T

# A function that calculates sum of marked element(s)
def sum_marked(arr, mark):
    S = 0
    for e, m in zip(arr, mark):
        S += e * m  # if m != 0 -> S += e
    
    return S

# A function that prints marked element(s)
def print_marked(arr, mark):
    for i, (e, m) in enumerate(zip(arr, mark)):
        if m != 0:
            print(f'{e}_({i})', end=' ')
    print()

# A function that finds subarrays having given sum
def find_subarray_sum(arr, S, mark = [], idx = 0):
    if idx == len(arr):
        if sum_marked(arr, mark) == S:
            print_marked(arr, mark)

        return
    
    find_subarray_sum(arr, S, mark + [0], idx + 1)

    find_subarray_sum(arr, S, mark + [1], idx + 1)

# Enter input
arr_inp = input('Enter a list (each number is separated by a space): ')
S = float(input('Enter T: '))

arr = [float(e) for e in arr_inp.strip().split()]

# Print output
find_subarray_sum(arr, S)