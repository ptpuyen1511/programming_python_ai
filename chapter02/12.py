# Problem: Write algorithm that proves we can represent division by subtraction

# Enter input
dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))

# Represent division by subtraction
quotient = 0
remainder = dividend
while remainder > divisor:
    quotient += 1
    remainder -= divisor

# Print output
print(f'{dividend} : {divisor} = {quotient} and {remainder}')