# Problem: Write an algorithm to input 2 segements [a, b] and [c, d] and print the intersection if non-empty

# Enter inputs
inp_1 = input('Insert first segment (two numbers seperated by space): ')
inp_2 = input('Insert second segment (two numbers seperated by space): ')

# Parse inputs
seg_1 = [int(x) for x in inp_1.split()]
seg_2 = [int(x) for x in inp_2.split()]

# Find intersection
num_in_seg_1 = set(x for x in range(seg_1[0], seg_1[1] + 1))
num_in_seg_2 = set(x for x in range(seg_2[0], seg_2[1] + 1))
intersection = list(num_in_seg_1.intersection(num_in_seg_2))

# Print output
if len(intersection) == 0:
    print('Empty intersection')
else:
    print('[' + str(intersection[0]) + ', ' + str(intersection[-1]) + ']')