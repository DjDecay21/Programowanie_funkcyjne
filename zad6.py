print("")
print("Zadanie 6")
fruit = ['apple', 'banana', 'orange', 'pear', 'avocado', 'grape']
numbers = [1,2,3,4,5,6,7,8,9]
def filtering(listOfFruit):
    print(list(filter(lambda x: x[0] == "a", listOfFruit)))

def maping(listOfNumber):
    print(list(map(lambda x: x*x, listOfNumber)))

filtering(fruit)
maping(numbers)