def print_min_max():
    lista_strings = ['AbC', 'dEf', '123', '456']
    lista_ints = [5, 2, 3, 4, 1]
    lista_floats = [6.2, 5.0, 7.1, 3.7, 20.5]
    tupla_strings = ('casa', 'pato', 'abacaxi', 'ganso', 'caçador')
    tupla_ints = (15, 12, 13, 14, 11)
    tupla_floats = (62.2, 52.0, 72.1, 32.7, 202.5)
    lista_diversos = ['AbC', '123', 3, 4, 7.0, 3.5]

    print(f'In list {lista_strings}, max is: {max(lista_strings)}, min is: {min(lista_strings)}\n')
    print(f'In list {lista_ints}, max is: {max(lista_ints)}, min is: {min(lista_ints)}\n')
    print(f'In list {lista_floats}, max is: {max(lista_floats)}, min is: {min(lista_floats)}\n')
    print(f'In tuple {tupla_strings}, max is: {max(tupla_strings)}, min is: {min(tupla_strings)}\n')
    print(f'In tuple {tupla_ints}, max is: {max(tupla_ints)}, min is: {min(tupla_ints)}\n')
    print(f'In tuple {tupla_floats}, max is: {max(tupla_floats)}, min is: {min(tupla_floats)}\n')

    # Mixed types - this might raise an error in Python 3 if types can't be compared directly
    try:
        print(f'In list {lista_diversos}, max is: {max(lista_diversos)}, min is: {min(lista_diversos)}\n')
    except TypeError:
        print(f'Cannot find min/max for mixed-type list: {lista_diversos} due to incompatible types.')

print_min_max()
