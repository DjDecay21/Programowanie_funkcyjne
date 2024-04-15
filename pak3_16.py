def remove_whitespace(string_list):
    return [string.strip() for string in string_list]


my_list = ["  hello ", "  world  ", "  python  "]
cleaned_list = remove_whitespace(my_list)
print(cleaned_list)