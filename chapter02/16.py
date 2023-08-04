# Problem: Write algorithm that calculates S = 1 + 2 + ... + n so that S > 1000

S = 0

while  S <= 1000:
    # Enter input
    n = int(input('Enter an integer: '))

    # Calculate sum
    S = 0
    for i in range(1, n + 1):
        S += i
    
# Print output
print(f'1 + 2 + ... + {n} = {S}')