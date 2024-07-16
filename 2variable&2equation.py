# Define the coefficients of the systems equation ax + by = c
a1, b1, c1 = 4, 2, 8
a2, b2, c2 = 5, 3, 9
# a1, b1, c1 = 1, 3, 6
# a2, b2, c2 = 2, 8, -12
# Calculate the determinant of the coefficient matrix
D = a1 * b2 - a2 * b1
# Calculate the determinants of the modified matrices
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
# Calculate the values of x and y
x = Dx / D
y = Dy / D
print(x, y)

def solve_systems(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    x = Dx / D
    y = Dy / D
    return x, y

print(solve_systems(4,2,8,5,3,9))
