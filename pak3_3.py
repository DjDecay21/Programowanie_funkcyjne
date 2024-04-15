def recursive_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total

nested_numbers = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
result = recursive_sum(nested_numbers)
print(result)