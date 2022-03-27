cubes = []
i = 0

while(True):
    cube = sorted(list(str(i ** 3)))
    cubes.append(cube)
    if(cubes.count(cube) == 5):
        print((cubes.index(cube)) ** 3)
        break
    i += 1