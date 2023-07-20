# A function that checks whether two rectangles intersect
def check_intersect(rect_1, rect_2):
    if rect_1[0] > rect_2[2] or rect_1[2] < rect_2[0] or rect_1[1] > rect_2[3] or rect_1[3] < rect_2[1]:
        return False

    return True

# A function that finds the area of two intersected rectangles
def find_intersection_area(rect_1, rect_2):
    # Check whether input rectangels intersect
    if not check_intersect(rect_1, rect_2):
        return 0
    
    # Calculate the intersection coordinates.
    x1 = max(rect_1[0], rect_2[0])
    y1 = max(rect_1[1], rect_2[1])
    x2 = min(rect_1[2], rect_2[2])
    y2 = min(rect_1[3], rect_2[3])

    # Calculate the intersection area.
    intersection_area = (x2 - x1) * (y2 - y1)

    return intersection_area

# Enter input
inp_1 = input('Enter the coordinates of the first rectangle (seperated by space): ')
inp_2 = input('Enter the coordinates of the second rectangle (seperated by space): ')

# Parse inputs
rect_1 = [float(x) for x in inp_1.split()]
rect_2 = [float(x) for x in inp_2.split()]

# Print output
print('The area intersection of the two rectangles is:', find_intersection_area(rect_1, rect_2))