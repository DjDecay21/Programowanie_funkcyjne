print("")
print("Zadanie 5")
numbers = list(range(1,11))
print("Cała lista: {}".format(numbers))
def zadanie_5(list):
    for i in list:
        if i % 2 == 0:
            print(i)
print("Parzyste liczby z tej listy")

#Wywołanie
zadanie_5(numbers)

a=5
b=6
pole = lambda a, b: a * b
print("Pole prostokąta")
print(pole(a,b))