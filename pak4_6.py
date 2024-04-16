def zastosuj_funkcje_do_listy(lista, funkcja):
    return [funkcja(element) for element in lista]

def podwoj(x):
    return x * 2

moja_lista = [1, 2, 3, 4, 5]
nowa_lista = zastosuj_funkcje_do_listy(moja_lista, podwoj)
print("Nowa lista:", nowa_lista)
