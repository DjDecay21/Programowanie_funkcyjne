def filtruj_parzyste(słownik):
    nowy_słownik = {}
    for klucz, wartość in słownik.items():
        if isinstance(wartość, int) and wartość % 2 == 0:
            nowy_słownik[klucz] = wartość
    return nowy_słownik

słownik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
nowy_słownik = filtruj_parzyste(słownik)
print(nowy_słownik)
