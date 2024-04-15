def capitalize_all_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

text = "hello world python"
capitalized_text = capitalize_all_words(text)
print(capitalized_text)
