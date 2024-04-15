def custom_sort(input_list, key_func=None):
    if key_func:
        return sorted(input_list, key=key_func)
    else:
        return sorted(input_list)

my_list = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_list = custom_sort(my_list, key_func=lambda x: x[0]) 
print(sorted_list)
