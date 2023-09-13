#squares = []
#for x in range(10):
#  squares.append(x**2)
#squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
print(squares)