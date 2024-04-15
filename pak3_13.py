def split_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunked_list = split_list(my_list, 3)
print(chunked_list)