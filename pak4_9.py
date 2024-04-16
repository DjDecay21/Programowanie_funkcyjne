def zastosuj_funkcje_do_krotek(lista_krotek, funkcja):
    return [funkcja(*krotka) for krotka in lista_krotek]

def dodaj_elementy_krotki(a, b):
    return a + b

lista_krotek = [(1, 2), (3, 4), (5, 6)]

wynik = zastosuj_funkcje_do_krotek(lista_krotek, dodaj_elementy_krotki)
print(wynik)
