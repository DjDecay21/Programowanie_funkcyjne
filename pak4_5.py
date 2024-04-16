def podziel_liste(lista, max_dl):
    result = []
    for i in range(0, len(lista), max_dl):
        result.append(lista[i:i + max_dl])
    return result

moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
podzielone_listy = podziel_liste(moja_lista, 3)
print(podzielone_listy)
