strings = ["jabłko", "banan", "truskawka", "ananas", "gruszka", "malina"]

def sort(litsOfString):
    sorted_list = sorted(litsOfString, key=lambda string: len(string))
    return sorted_list
print(sort(strings))