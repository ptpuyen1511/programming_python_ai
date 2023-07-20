# Problem: Write algorithm that inputs n rectangles and then outputs two rectangles that have the largest intersection area.

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

# A function that finds the largest area of two intersected rectangles in a list of rectangles
def find_rects_largest_intersection_area(list_rects):
    res_area = 0
    res_rects = []

    for i in range(len(list_rects)):
        for j in range(i + 1, len(list_rects)):
            rect_1 = list_rects[i]
            rect_2 = list_rects[j]
            
            area = find_intersection_area(rect_1, rect_2)

            # Update largest intersection
            if area > res_area:
                res_area = area
                res_rects = [rect_1, rect_2]

    return res_rects

# Enter input
n = int(input('How many rectangles do you have? '))

list_rects = []
for i in range(n):
    inp = input(f'Enter the coordinates of rectangle {i+1} (seperated by space): ')
    rect = [float(x) for x in inp.split()]
    list_rects.append(rect)

# Print output
print('Two rectangles that have largest intersection area: ', find_rects_largest_intersection_area(list_rects))