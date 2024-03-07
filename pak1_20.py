def analyze_data(data):
    if isinstance(data, list):
        print("To jest lista o długości:", len(data))
    elif isinstance(data, tuple):
        print("To jest krotka o rozmiarze:", len(data))
    else:
        print("To jest inna struktura danych")

analyze_data([1, 2, 3])
analyze_data((1, 2, 3, 4))
analyze_data({1, 2, 3})