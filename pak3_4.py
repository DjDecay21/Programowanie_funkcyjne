def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list = [1, 2, 3, 2, 4, 1, 5, 6, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)