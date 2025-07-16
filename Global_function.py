# Global variable
x = '123'

def test_global_read() -> None:
    print(f'Value of x inside test_global_read(): {x}')

test_global_read()
print(f'Value of x outside function: {x}')
print('---')

def test_global_modify() -> None:
    global x
    x = x + '456'  # Modify global x
    print(f'Value of x inside test_global_modify(): {x}')

test_global_modify()
print(f'Value of x outside function after modification: {x}')
print('---')

x = 10

def test_local_variable() -> None:
    x = 20  # Local variable x
    print(f'Value of local variable x inside test_local_variable(): {x}')

test_local_variable()
print(f'Value of global variable x outside function: {x}')
