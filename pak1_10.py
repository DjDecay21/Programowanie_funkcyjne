def evenNumberGenerator():
    n=0
    while True:
        yield n
        n+=2
gen = evenNumberGenerator()
first=[next(gen) for _ in range(10)]
print (first)