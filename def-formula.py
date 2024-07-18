def solve_and_print_quadratic(example):
    a = example["a"]
    b = example["b"]
    c = example["c"]
    
    x1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    
    print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")
    print(f"The solutions are: x1 = {x1}, x2 = {x2}")

def solve_and_print_systems(example):
    a1 = example["a1"]
    b1 = example["b1"]
    c1 = example["c1"]
    a2 = example["a2"]
    b2 = example["b2"]
    c2 = example["c2"]
    
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    
    if D == 0:
        if Dx == 0 and Dy == 0:
            print("The system has infinitely many solutions.")
        else:
            print("The system has no solution.")
    else:
        x = Dx / D
        y = Dy / D
        print(f"The system of equations is: {a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2}")
        print(f"The solutions are: x = {x}, y = {y}")

# รับค่าจากผู้ใช้สำหรับ example0
example0 = {}
example0["a"] = float(input("Enter the coefficient a: "))
example0["b"] = float(input("Enter the coefficient b: "))
example0["c"] = float(input("Enter the coefficient c: "))
example0["a1"] = float(input("Enter the coefficient a1: "))
example0["b1"] = float(input("Enter the coefficient b1: "))
example0["c1"] = float(input("Enter the coefficient c1: "))
example0["a2"] = float(input("Enter the coefficient a2: "))
example0["b2"] = float(input("Enter the coefficient b2: "))
example0["c2"] = float(input("Enter the coefficient c2: "))

example1 = {"a": 1, "b": -5, "c": 6}
example2 = {"a": 2, "b": 4, "c": -6}
example3 = {"a": 1, "b": 3, "c": -10}
example4 = {"a1": 1, "b1": 1, "c1": 5, "a2": 2, "b2": -1, "c2": 1}
example5 = {"a1": 3, "b1": 2, "c1": 12, "a2": 4, "b2": -1, "c2": 5}
example6 = {"a1": 6, "b1": -3, "c1": 9, "a2": 2, "b2": 1, "c2": 5}

# เลือกตัวอย่างที่ต้องการ
selected_example = example0  # คุณสามารถเปลี่ยนเป็น example1, example2, example3

# เรียกใช้ฟังก์ชัน
solve_and_print_quadratic(selected_example)
solve_and_print_systems(selected_example)
