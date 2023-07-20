# Method 1: Use instruction
def is_palindrome_1(n):
    if n < 0:
        n *= -1

    num_in_list = list(str(n))
    len_n = len(num_in_list)

    for i in range(int(len_n/2)):
        if num_in_list[i] != num_in_list[len_n - 1 - i]:
            return False
        
    return True

# Method 2: Convert to string, check whether a string is palindrome
def is_palindrome_2(n):
    if n < 0:
        n *= -1

    rev_n = str(n)[::-1]

    return str(n) == rev_n

# Enter input
n = int(input('Enter an integer: '))

# Print output
print(f'Is {n} palindrome? -> (1)', is_palindrome_1(n))
print(f'Is {n} palindrome? -> (2)', is_palindrome_2(n))