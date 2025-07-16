def demonstrate_variable_assignment():
    # Variables can hold values and be reassigned freely
    x = 1
    x, y, z = [1, 2, 3]
    y = 10
    x = y  # x now holds 10

    # Strings are immutable: attempting to modify a character raises an error
    name = "python"
    try:
        name[0] = "j"
    except TypeError as e:
        print(f"Error: {e} (Strings are immutable)")

    # To 'modify' a string, create a new one using slicing and concatenation
    name = "j" + name[1:]
    print(f"Modified string by slicing and concatenation: {name}")

    # Assign string to a class attribute (example)
    class Example:
        def __init__(self, name):
            self.name = name

    obj = Example(name)
    print(f"Object attribute name: {obj.name}")

demonstrate_variable_assignment()

"""That error message confirms that strings in Python cannot be changed character-by-character (they’re immutable)."""