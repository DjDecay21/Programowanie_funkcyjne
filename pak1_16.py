def compose(f, g):
    return lambda x: f(g(x))
h = lambda x: x * 2
k = lambda x: x + 3
composed_function = compose(h, k)
print (composed_function(5))