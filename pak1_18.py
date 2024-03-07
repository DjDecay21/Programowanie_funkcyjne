def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

even_gen = even_numbers()
for _ in range(5):
    print(next(even_gen))

