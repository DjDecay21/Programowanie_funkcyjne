lista = [1,2,3,4,5,6,7,8,9]
def func(lista):
    for i in lista:
        if i%2!=0:
            lista.remove(i)
    print(lista)

func(lista)