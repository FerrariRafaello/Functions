def basic_sort_examples():
    # Sorting a list of integers
    num_list = [10, 5, 11, 3, 20, 18]
    print("Sorted list:", sorted(num_list))  # ascending order

    # Sorting a tuple of strings
    languages = ("python", "java", "ruby", "php", "golang")
    print("Sorted tuple:", sorted(languages))  # alphabetical order

    # Sorting a dictionary by keys
    my_dict = {1: "b", 2: "a", 3: "c"}
    print("Sorted dictionary keys:", sorted(my_dict))  # keys sorted

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})" if self.age is not None else self.name

def sort_people_by_name(people):
    return sorted(people, key=lambda person: person.name)

def sort_people_by_age(people, reverse=False):
    return sorted(people, key=lambda person: person.age, reverse=reverse)

def demonstrate_object_sorting():
    p1 = Person("Marcos", 28)
    p2 = Person("Joao", 30)
    p3 = Person("Ana", 25)

    people = [p1, p2, p3]

    print("Sorted by name:", sort_people_by_name(people))
    print("Sorted by age:", sort_people_by_age(people))
    print("Sorted by age descending:", sort_people_by_age(people, reverse=True))

    # Alternative way to reverse sort with slicing
    print("Sorted by age reversed with slicing:", sort_people_by_age(people)[::-1])

if __name__ == "__main__":
    basic_sort_examples()
    demonstrate_object_sorting()
