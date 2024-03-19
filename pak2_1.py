from itertools import product

lista1 = ['A', 'B']
lista2 = ['C', 'D']

kombinacje = list(product(lista1, lista2))

for kombinacja in kombinacje:
    print(kombinacja)
