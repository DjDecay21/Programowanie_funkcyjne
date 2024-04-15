x=int(input("Podaj x"))
y=int(input("Podaj y"))
z=int(input("Podaj z"))
average_lambda = lambda x, y, z: (x + y + z) / 3
print(average_lambda(x,y,z))

print(average_lambda(6,15,15))

print(average_lambda(5,10,15))

print(average_lambda(2, 4, 6))