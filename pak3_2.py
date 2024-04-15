def filter_long_words(list_of_words):
    average_length = sum(len(word) for word in list_of_words) / len(list_of_words)

    filtered_words = [word for word in list_of_words if len(word) > average_length]

    return filtered_words

words = ["apple", "banana", "orange", "kiwi", "strawberry"]
filtered_words = filter_long_words(words)
print(filtered_words)