import math

def check_right_triangle(sides):
    # Sort sides to identify the longest side easily
    a, b, c = sorted(sides)

    # Check triangle inequality: sum of smaller sides > largest side
    if a + b <= c:
        return "The given sides do not form a triangle."

    # Check Pythagoras theorem for right triangle
    if math.isclose(c**2, a**2 + b**2, rel_tol=1e-9):
        return f"The sides {a}, {b}, and {c} form a right triangle."
    else:
        return "The sides form a triangle, but not a right triangle."

# Example usage:
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

result = check_right_triangle([side1, side2, side3])
print(result)
