def input_numbers(n=5):
    numbers = []  # to store input numbers as strings
    
    for _ in range(n):
        num = input('Enter a number: ')
        numbers.append(num)
    
    print('Numbers entered:', numbers)

input_numbers()
