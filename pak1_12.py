from functools import partial

def razyTrzy(number, three):
    return number*three
number = partial(razyTrzy,three = 3)
print (number(2))