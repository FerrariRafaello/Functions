def sequence_unpacking_demo():
    # Unpacking a list into variables
    x, y, z = [1, 2, 3]
    print(f"x:{x}, y:{y}, z:{z}")

    # Unpacking a tuple and ignoring the last element using underscore
    x1, y1, _ = (1, 2, 3)
    print(f"x:{x1}, y:{y1}")

    # Using * to capture multiple elements in a list unpacking
    *n1, n2 = [9, 4, 5, 15, 20]
    print(n1, n2)

    n3, *n4 = [9, 4, 5, 15, 20]
    print(n3, n4)

    # Example with a list of grades
    grades = [9, 7, 8, 5, 10]
    print(grades[1:4])  # slice from index 1 to 3

    # Unpack with * capturing middle elements
    n1, *n2, n3 = grades
    print(n2)

    # Get only first and last element via slicing with step
    print(grades[::4])
    print(n1, n3)


# Call the function to run the demo
sequence_unpacking_demo()
