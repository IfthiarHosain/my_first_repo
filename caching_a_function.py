squares={}
for i in range(1,11):
    if (square := i**2) not in squares:
        squares[square]=i
print(square)

