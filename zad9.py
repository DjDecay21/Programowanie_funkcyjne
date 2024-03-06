print("")
print("Zadanie 9")
import functools
numbers = [5,4,3,2,5,6,87,64,21,10]
average = functools.reduce(lambda x, y: sum(numbers)/len(numbers), numbers)
print(average)

max_value = functools.reduce(lambda x, y: max(numbers), numbers)
print(max_value)
