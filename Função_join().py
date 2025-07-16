def join_collections(separator: str, lst: list, tpl: tuple, dct: dict):
    print('List:', lst)
    print('Tuple:', tpl)
    print('Dictionary keys:', list(dct.keys()))
    
    print('Joined list:', separator.join(lst))
    print('Joined tuple:', separator.join(tpl))
    print('Joined dictionary keys:', separator.join(dct.keys()))


# Example usage:
my_list = ['A_list', 'B_list', 'C_list']
my_tuple = ('A_tuple', 'B_tuple', 'C_tuple')
my_dict = {'A_dict': '1', 'B_dict': '2', 'C_dict': '3'}
sep = '*'

join_collections(sep, my_list, my_tuple, my_dict)
