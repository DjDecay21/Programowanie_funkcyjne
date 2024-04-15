def partition_list(input_list, condition):
    satisfied = []
    remaining = []
    for item in input_list:
        if condition(item):
            satisfied.append(item)
        else:
            remaining.append(item)
    return satisfied, remaining

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = partition_list(numbers, is_even)
print("Parzyste liczby:", even_numbers)
print("Nieparzyste liczby:", odd_numbers)
