import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania {func.__name__}: {end_time - start_time} sekund")
        return result
    return wrapper

lista = [1,2,3,4,5,6,7,8,9]
@timeit
def func(lista):
    for i in lista:
        if i%2!=0:
            lista.remove(i)
    print(lista)

func(lista)

timeit(func)