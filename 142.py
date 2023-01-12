squares = [i**2 for i in range(1, 1000)]
for x in range(1, 10000):
    for y in range(1, x):
        for z in range(1, y):
            if x+y in squares and y+z in squares and x+z in squares and x-y in squares and x-z in squares and y-z in squares:
                print(x,y,z)