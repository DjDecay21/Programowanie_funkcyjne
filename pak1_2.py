
def make_multiple(x):
    def multipler(n):
        return x*n

    return multipler


double = make_multiple(2)

print(double(5))