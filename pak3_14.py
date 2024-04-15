def count_unique_elements(input_list):
    unique_elements = set(input_list)
    return len(unique_elements)

my_list = [1, 2, 3, 4, 1, 2, 3, 5]
unique_count = count_unique_elements(my_list)
print(unique_count)