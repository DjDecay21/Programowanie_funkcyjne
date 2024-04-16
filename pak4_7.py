def polacz_słowniki(*słowniki):
    wynik = {}
    for słownik in słowniki:
        for klucz, wartość in słownik.items():
            if klucz in wynik:
                wynik[klucz] += wartość
            else:
                wynik[klucz] = wartość
    return wynik

słownik1 = {'a': 1, 'b': 2, 'c': 3}
słownik2 = {'b': 3, 'c': 4, 'd': 5}
słownik3 = {'c': 5, 'd': 6, 'e': 7}

wynik = polacz_słowniki(słownik1, słownik2, słownik3)
print(wynik)
