# Problem: Write program to calculate the area of a polygon with n sides given its n vertices

# A function that calculates the area of polygon using Shoelace formula
def calc_area_polygon(list_x, list_y):
    area = 0 

    n = len(list_x)
    
    list_x.append(list_x[0]), list_y.append(list_y[0])
    for i in range(n):
        area += (list_y[i] + list_y[i + 1]) * (list_x[i] - list_x[i + 1])

    # # Another way
    # j = n - 1
    # for i in range(n):
    #     area += (list_x[i + 1] + list_x[i]) * (list_y[j] - list_y[i])
    #     j = i
    
    return abs(area) / 2

# Enter input
inp_1 = input('Enter list of xi (separated by space): ')
inp_2 = input('Enter list of yi (separated by space): ')

list_x = [int(x) for x in inp_1.split()]
list_y = [int(y) for y in inp_2.split()]

# Print output
print('The area is:', calc_area_polygon(list_x, list_y))