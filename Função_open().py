import pprint

def read_file_examples(filename: str):
    with open(filename, 'r') as file:
        print('\nUsing read():')
        content = file.read()
        print(content)

        file.seek(0)  # Reset pointer to beginning

        print('\nUsing readline():')
        line = file.readline()
        print(line)

        file.seek(0)

        print('\nUsing readlines():')
        lines = file.readlines()
        pprint.pprint(lines)

    print('\nReading file line-by-line in a loop:')
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

    # Counting the number of lines
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)
    print(f'\nNumber of lines in file: {line_count}')

# Example usage
read_file_examples('contatos.txt')
