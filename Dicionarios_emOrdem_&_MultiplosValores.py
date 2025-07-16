from collections import defaultdict, OrderedDict

def multdict_demo():
    """
    Demonstrates usage of defaultdict with list and set,
    and OrderedDict for maintaining insertion order.
    """

    # defaultdict with list: multiple values per key, allows duplicates
    d_list = defaultdict(list)
    d_list["marcos"].append(10)
    d_list["marcos"].append(20)
    d_list["marcos"].append(30)
    print("List defaultdict for 'marcos':", d_list["marcos"])
    print("Complete defaultdict (list):", d_list)

    d_list["joao"].extend([1, 2, 3])
    print("List defaultdict for 'joao':", d_list["joao"])
    print("Complete defaultdict (list):", d_list)

    # defaultdict with set: multiple values per key, no duplicates
    d_set = defaultdict(set)
    d_set["marcos"].add(10)
    d_set["marcos"].add(10)  # duplicate, will be ignored
    d_set["marcos"].add(20)
    d_set["marcos"].add(30)
    print("Set defaultdict for 'marcos':", d_set["marcos"])
    print("Complete defaultdict (set):", d_set)

    # OrderedDict preserves insertion order when iterating
    d_ordered = OrderedDict()
    d_ordered["python"] = 10
    d_ordered["java"] = 5
    d_ordered["php"] = 6
    d_ordered["C"] = 10

    print("OrderedDict iteration:")
    for key in d_ordered:
        print(f"{key}: {d_ordered[key]}")

    """
    Regular dicts in Python 3.7+ maintain insertion order as well,
    but OrderedDict explicitly guarantees this behavior and has
    some additional features.
    """

# Run the demo
multdict_demo()
