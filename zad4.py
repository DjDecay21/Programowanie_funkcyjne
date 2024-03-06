import zad3
print("")
print("Zadanie 4")
name = zad3.name
def zadanie_4(zadanie_3, name):
    print("Funcja zwraca tę wiadomosc i zawartosc funkcji zadanie_3 + ")
    zadanie_3(name)

#Wywołanie
zadanie_4(zad3.zadanie_3, name)