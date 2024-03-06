print("")
print("Zadanie 8")
squares = [x**2 for x in range(1, 11)]
print(squares)
squares_to_string = [str(word) for word in squares]
word_lengths = [len(word) for word in squares_to_string]

print(word_lengths)