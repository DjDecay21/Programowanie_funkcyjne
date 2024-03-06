print("")
print("Zadanie 7")
numbers = [1,2,3,4,5,6,7,8,9]
def pow_number(numbers):
    return numbers * numbers
def add_five(numbers):
    return numbers + 5
def apply_two(numbers):
    numbers = map(pow_number, numbers)
    numbers = map(add_five, numbers)
    return list(numbers)

print(apply_two(numbers))
def zadanie_7(function, arguments):
    for f, v in zip(function, arguments):
        print(f(*v) if isinstance(v, tuple) else (f(v)))
#zadanie_7([pow_number, add_five], [1,2,3,4,5,6,7,8,9])