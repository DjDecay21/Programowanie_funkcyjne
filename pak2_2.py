#2) Napisz funkcję, która przyjmuje listę elementów i zwraca listę wszystkich możliwych 2-elementowych kombinacji tych elementów.
import itertools

list1 = [1, 2, 3, 4]

print(list(itertools.permutations(list1, r=2)))