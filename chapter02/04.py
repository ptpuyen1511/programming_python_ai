# Problem: Write algorithm that calculates average of integers. Enter 0 to finish entering integers

sum = 0
n = 0

# Enter input
inp = -1
while inp != 0:
    inp = int(input('Enter an integer (enter 0 to terminate): '))

    if inp != 0:
        sum += inp
        n += 1

avg = sum / n

# Print output
print('The average of input integers: ', avg)