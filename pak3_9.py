def zip_with_index(input_list):
    return [(item, index) for index, item in enumerate(input_list)]


my_list = ['a', 'b', 'c', 'd']
result = zip_with_index(my_list)
print(result)
