def find_max_min_diff(input_list):
    if not input_list:
        return None 
    max_val = max(input_list)
    min_val = min(input_list)
    return max_val - min_val


my_list = [1, 2, 5, 10, 7, 3]
result = find_max_min_diff(my_list)
print(result)
