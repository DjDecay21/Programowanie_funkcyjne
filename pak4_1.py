def suma_parzystych(lista):
    suma = 0
    for liczba in lista:
        if liczba % 2 == 0:
            suma += liczba
    return suma

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_parzystych_liczb = suma_parzystych(liczby)
print(suma_parzystych_liczb)
