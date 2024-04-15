from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = {key: list(group) for key, group in groupby(numbers, key=lambda x: x % 2 == 0)}

for is_even, group in result.items():
    print(f"{'Parzyste' if is_even else 'Nieparzyste'}: {group}")
