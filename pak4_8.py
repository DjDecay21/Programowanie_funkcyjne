from collections import Counter

def najczesciej_wystepujacy_element(lista):
    licznik = Counter(lista)
    najczestszy_element = max(licznik, key=licznik.get)
    return najczestszy_element

moja_lista = [1, 2, 3, 4, 2, 2, 1, 4, 4, 4]
najczestszy = najczesciej_wystepujacy_element(moja_lista)
print(najczestszy)
