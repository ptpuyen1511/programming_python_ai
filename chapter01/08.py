# Problem: Let x1, ..., xn and y1, ..., yn with xi, yi present a segment [xi, yi].
# Write an algorithm that input n segments and then outputs two segments that have the largest intersection.

# A function that finds intersection of two segments
def find_intersection(seg_1, seg_2):
    # Find intersection
    num_in_seg_1 = set(x for x in range(seg_1[0], seg_1[1] + 1))
    num_in_seg_2 = set(x for x in range(seg_2[0], seg_2[1] + 1))
    intersection = list(num_in_seg_1.intersection(num_in_seg_2))

    if len(intersection) == 0:
        return None
    else:
        return [intersection[0], intersection[-1]]

# A function that finds the largest intersection of two segments in a list of segments
def find_segments_largest_intersection(list_x, list_y):
    res_intersection = [0, 0]
    res_segments = []

    for i in range(len(list_x)):
        for j in range(i + 1, len(list_x)):
            seg_1 = [list_x[i], list_y[i]]
            seg_2 = [list_x[j], list_y[j]]
            
            intersection = find_intersection(seg_1, seg_2)

            # Two segments are not overlap
            if intersection == None:
                continue

            # Update largest intersection
            if (intersection[-1] - intersection[0]) > (res_intersection[-1] - res_intersection[0]):
                res_intersection = intersection
                res_segments = [seg_1, seg_2]

    return res_segments

# Enter input
inp_1 = input('Enter list of xi (separated by space): ')
inp_2 = input('Enter list of yi (separated by space): ')

list_x = [int(x) for x in inp_1.split()]
list_y = [int(y) for y in inp_2.split()]

# Print output
print('Two segments that have largest intersection: ', find_segments_largest_intersection(list_x, list_y))
