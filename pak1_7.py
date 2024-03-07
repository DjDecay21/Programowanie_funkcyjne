names = ["Anna","Piotrek","Michał","Ola","Paulina"]
filterNames = list(filter(lambda x: len(x) > 5, names))
print (filterNames)