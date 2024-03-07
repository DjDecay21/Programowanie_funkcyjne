def add(x):
    def inner(y):
        return x + y
    return inner
print(add(5)(2))