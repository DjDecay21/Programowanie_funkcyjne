def rotate_list(input_list, steps):
    length = len(input_list)
    if length == 0:
        return input_list
    steps %= length
    return input_list[-steps:] + input_list[:-steps]


my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)
print(rotated_list)
