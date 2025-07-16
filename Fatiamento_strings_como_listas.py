def string_slicing_demo():
    text = 'Ser ou não ser, eis a questão'
    # Indices:  01234567891123456789212345678

    # Access a single character by index
    print(text[28])  # prints character at position 28

    print('Full text:', text)

    print('Slicing text directly:')
    print('text[0:3] =', text[0:3])  # characters from index 0 to 2

    print('Omitting the start index:')
    print('text[:3] =', text[:3])  # same as above, from start to index 2

    print('Slicing with negative indices:')
    print('text[-7:] =', text[-7:])  # last 7 characters

    print('Slicing text in the middle:')
    print('text[7:14] =', text[7:14])  # characters from index 7 to 13

# Run the demo
string_slicing_demo()
