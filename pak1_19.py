def multiply_elements(tuple_data, multiplier):
    multiplied_tuple = tuple(element * multiplier for element in tuple_data)
    return multiplied_tuple

original_tuple = (1, 2, 3, 4, 5)
multiplier = 2
result_tuple = multiply_elements(original_tuple, multiplier)
print(result_tuple)  