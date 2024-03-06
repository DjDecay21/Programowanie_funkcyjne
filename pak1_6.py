list1=[1,2,3,4,5,6,7,8]
def sqrt(x):
    return x*x
squared_numbers = list(map(sqrt, list1))

print(squared_numbers)