def map_nested(func, nested_list):
    mapped_list = []
    for item in nested_list:
        if isinstance(item, list):
            mapped_list.append(map_nested(func, item))
        else:
            mapped_list.append(func(item))
    return mapped_list


def square(x):
    return x ** 2

nested_list = [1, [2, 3], [4, 5, 6], 7]
mapped_result = map_nested(square, nested_list)
print(mapped_result)
