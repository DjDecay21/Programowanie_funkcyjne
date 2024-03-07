from functools import partial
import operator

add_five = partial(operator.add, 5)
result = add_five(7)
print(result)