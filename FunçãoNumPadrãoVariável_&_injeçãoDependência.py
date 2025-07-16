# Function with variable-length positional arguments (*args)
def print_args(*args):
    print("Positional arguments (tuple):", args)

print_args(1, 2, 3, "marcos")


# Function with variable-length keyword arguments (**kwargs)
def print_kwargs(**kwargs):
    print("Keyword arguments (dict):", kwargs)

print_kwargs(name="marcos", age=28, language="python")


# Function that iterates over keyword arguments cleanly
def print_kwargs_items(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs_items(syllable="tonic", teacher="accordion", day="pirate")


# Dependency Injection explanation and example
languages = ["python", "php", "c", "ruby", "lua"]

# Sorting languages by length using 'key' parameter
sorted_languages = sorted(languages, key=len)
print("Languages sorted by length:", sorted_languages)
