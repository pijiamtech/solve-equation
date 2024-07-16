def solve_quadratic(a, b, c):
    x1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    return x1, x2

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")
solutions = solve_quadratic(a, b, c)
print(f"The solutions are: x1 = {solutions[0]}, x2 = {solutions[1]}")


def solve_systems(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    x = Dx / D
    y = Dy / D
    return x, y

a1 = int(input("Enter the coefficient a1: "))
b1 = int(input("Enter the coefficient b1: "))
c1 = int(input("Enter the coefficient c1: "))
a2 = int(input("Enter the coefficient a2: "))
b2 = int(input("Enter the coefficient b2: "))
c2 = int(input("Enter the coefficient c2: "))
print(f"The quadratic equation is: {a1}x + {b1}y = {c1} ")
print(f"The quadratic equation is: {a2}x + {b2}y = {c2} ")
solutions = solve_systems(a1, b1, c1, a2, b2, c2)
print(f"The solutions are: x = {solutions[0]}, y = {solutions[1]}")