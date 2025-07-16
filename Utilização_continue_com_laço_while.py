def letter_input_loop():
    while True:
        letter = input('Enter a letter different from "x" ("q" to quit): ')
        if letter == 'x':
            continue  # skip printing and ask again
        elif letter == 'q':
            break  # exit loop
        else:
            print(f'You entered the letter {letter}')
    
    print('End of program!')

letter_input_loop()
