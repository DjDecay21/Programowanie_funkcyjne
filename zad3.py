from datetime import date
print("")
print("Zadanie 3")
def zadanie_3(name):
    year = date.today().year
    print("Hello {}".format(name))
    print("Now is {} year".format(year))
name = "Michał"

#Wywołanie
zadanie_3(name)