# def solve_quadratic(a, b, c):
#     x1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
#     x2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
#     return x1, x2

# example1 = {
#     "a": 1, "b": -5, "c": 6
# }

# # เรียกใช้ฟังก์ชัน solve_quadratic ด้วยค่าจาก dictionary example1
# solutions = solve_quadratic(example1["a"], example1["b"], example1["c"])

# print(f"The quadratic equation is: {example1['a']}x^2 + {example1['b']}x + {example1['c']} = 0")
# print(f"The solutions are: x1 = {solutions[0]}, x2 = {solutions[1]}")

def solve_and_print_quadratic(example):
    a = example["a"]
    b = example["b"]
    c = example["c"]
    
    x1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    
    print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")
    print(f"The solutions are: x1 = {x1}, x2 = {x2}")

example1 = {"a": 1, "b": -5, "c": 6}
example2 = {"a": 2, "b": 4, "c": -6}
example3 = {"a": 1, "b": 3, "c": -10}
example4 = {"a": 3, "b": -12, "c": 9}
example5 = {"a": 1, "b": -4, "c": -12}

solve_and_print_quadratic(example5)
