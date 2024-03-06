print("")
print("Zadanie 10")

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Użycie generatora
fib_gen = fibonacci_generator()
#range(x) podaj ile liczb chcesz wypisać
for _ in range(10):
    print(next(fib_gen))


def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# Użycie generatora
print("")
print("text.txt")
file_path = 'text.txt'
lines_generator = read_large_file(file_path)
try:
    for _ in range(10):
        print(next(lines_generator))
except StopIteration:
    print("")