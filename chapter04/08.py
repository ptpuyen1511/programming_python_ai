# Problem: Write program to convert decimal to binary number

# A function that converts binary number form decimal number
def decimal_to_binary(n):
    if n == 0:
        return ''
    
    return decimal_to_binary(n // 2) + str(n % 2)

# Enter input
n = int(input('Enter a number: '))

# Print output
print(f'{n} (10) -> {decimal_to_binary(n)} (2)')