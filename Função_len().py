def print_collections_info(lst: list, tpl: tuple, dct: dict, string: str):
    print('List:', lst, 'Length:', len(lst))
    print('Tuple:', tpl, 'Length:', len(tpl))
    print('Dictionary:', dct, 'Length:', len(dct))
    print('String:', string, 'Length:', len(string))


# Example usage:
my_list = ['A_list', 'B_list', 'C_list']
my_tuple = ('A_tuple', 'B_tuple', 'C_tuple')
my_dict = {'A_dict': '1', 'B_dict': '2', 'C_dict': '3'}
my_string = 'Two Grapes'

print_collections_info(my_list, my_tuple, my_dict, my_string)
