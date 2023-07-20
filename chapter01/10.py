# Import package
from collections import Counter

# A function that checks whether two strings are permutations of each other
def is_permutation(str_1, str_2):
    chars_in_str_1 = Counter(str_1)
    chars_in_str_2 = Counter(str_2)

    # Two strings are permutations of each other if and only if they have the same frequency of characters.
    return chars_in_str_1 == chars_in_str_2

# Enter input
str_1 = input('Enter the first string: ')
str_2 = input('Enter the second string: ')

# Print output
if is_permutation(str_1, str_2):
    print(f'{str_1} is a permuation of {str_2}')
else:
    print('Two strings are not permuation of each other')