# Algorithm: Write algorithm that find the maximum number of the list of input numbers

max = -float('inf')

# Enter input
inp = -1
while inp != 0:
    inp = int(input('Enter an integer (enter 0 to terminate): '))

    if inp > max:
        max = inp

# Print output
print('The maximum number is: ', max)