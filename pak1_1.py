def apply_twice2(double, value):
    return double(double(value))

result = apply_twice2(lambda num: num*2, 2)

print(result)
