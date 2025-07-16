def check_alpha(text: str):
    if text.isalpha():
        print(f'The text "{text}" contains only letters.')
    else:
        print(f'The text "{text}" contains non-alphabetic characters.')


# Example usage:
check_alpha('TinhaUmaPedraNoMeioDoCaminho')
check_alpha('Tinha 2 pedras no meio do caminho')
