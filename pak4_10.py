def generuj_permutacje(lista):
    if len(lista) <= 1:
        return [lista]

    wszystkie_permutacje = []
    for i in range(len(lista)):
        reszta = lista[:i] + lista[i + 1:]
        for perm in generuj_permutacje(reszta):
            wszystkie_permutacje.append([lista[i]] + perm)

    return wszystkie_permutacje


moja_lista = [1, 2, 3]
wynik = generuj_permutacje(moja_lista)
print(wynik)
