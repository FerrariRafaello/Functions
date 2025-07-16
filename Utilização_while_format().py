def powers_of_two():
    n = int(input("Enter the maximum exponent n: "))
    for i in range(n + 1):
        print(f"2^{i} = {2**i}")
    print("End")

def find_max_number():
    max_value = float('-inf')  # Initialize to smallest possible value
    quantity = int(input("Enter how many numbers you will input: "))
    
    for i in range(1, quantity + 1):
        num = int(input(f"Enter value {i}: "))
        if num > max_value:
            max_value = num
    
    print(f"The maximum number entered was: {max_value}")

# Example calls:
powers_of_two()
find_max_number()
