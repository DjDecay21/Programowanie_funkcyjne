def cumulative_sum(input_list):
    cumulative = []
    total = 0
    for num in input_list:
        total += num
        cumulative.append(total)
    return cumulative


my_list = [1, 2, 3, 4, 5]
result = cumulative_sum(my_list)
print(result)
