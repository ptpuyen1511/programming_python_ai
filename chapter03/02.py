# Problem: Write program to solve quadratic equation

def solve_quadratic(a, b, c):
    # Linear equation
    if a == 0:
        if b == 0:
            if c == 0:
                return -1, []       # infinitely many solutions
            else:
                return 0, []        # no solutions
        else:
            return 1, [-c/b]        # one solution
    
    delta = b**2 - 4 * a * c

    # Quadratic equation
    if delta < 0:
        return 0, []                # no real solutions
    elif delta == 0:
        return 1, [-b / (2 * a)]    # one repeated solution
    
    return 2, [(-b + delta**0.5)/(2*a), (-b - delta**0.5)/(2*a)] # two distinct solutions

# Enter input
print('Program to solve quadratic equation ax^2 + bx + c = 0')
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

num_sol, sol = solve_quadratic(a, b, c)

# Print output
if num_sol == -1:
    print('This equation has infinitely many solutions')
elif num_sol == 0:
    print('This equation has no solutions')
elif num_sol == 1:
    print('This equation has one solution', sol[0])
else:
    print('This equation has two solutions:', sol[0], 'and', sol[1])