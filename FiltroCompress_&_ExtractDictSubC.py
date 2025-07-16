from itertools import compress

def filter_names_by_value(names, values, threshold):
    bool_mask = [v > threshold for v in values]
    return list(compress(names, bool_mask))

def filter_dict_by_value(d, threshold, greater=True):
    if greater:
        return {k: v for k, v in d.items() if v > threshold}
    else:
        return {k: v for k, v in d.items() if v < threshold}


# Example usage:
if __name__ == "__main__":
    names = ["marcos", "joao", "maria", "pedro"]
    values = [10, 5, 6, 2]
    filtered_names = filter_names_by_value(names, values, 5)
    print("Filtered names (values > 5):", filtered_names)

    prices = {"iphone": 2500, "notebook": 2000, "mouse": 90, "keyboard": 70}
    expensive_items = filter_dict_by_value(prices, 100, greater=True)
    print("Expensive items (>100):", expensive_items)
    cheap_items = filter_dict_by_value(prices, 100, greater=False)
    print("Cheap items (<100):", cheap_items)
