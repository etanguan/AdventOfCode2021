def check(c, coords):
    if coords.count(c) == 1:
        return 1
    else:
        return 0

a = input().rstrip().split()
coords = []
won = []
counter = 0
while a != ['n']:
    coord1 = a[0].split(',')
    coord1 = [int(i) for i in coord1]
    coord2 = a[2].split(',')
    coord2 = [int(i) for i in coord2]
    if coord1[0] == coord2[0]:
        if coord1[1] > coord2[1]:
            for i in range(coord1[1] - coord2[1]+1):
                counter += check([coord1[0], coord2[1]+i], coords)
                coords.append([coord1[0], coord2[1]+i])
        else:
            for i in range(coord2[1] - coord1[1]+1):
                counter += check([coord2[0], coord1[1]+i], coords)
                coords.append([coord2[0], coord1[1]+i])
    elif coord1[1] == coord2[1]:
        if coord1[0] > coord2[0]:
            for i in range(coord1[0] - coord2[0]+1):
                counter += check([coord2[0]+i, coord1[1]], coords)
                coords.append([coord2[0]+i, coord1[1]])
        else:
            for i in range(coord2[0] - coord1[0]+1):
                counter += check([coord1[0]+i, coord2[1]], coords)
                coords.append([coord1[0]+i, coord2[1]])
    else:
        if coord1[0] > coord2[0] and coord1[1] < coord2[1]:
            for i in range(coord1[0]-coord2[0]+1):
                counter += check([coord1[0]-i, coord1[1]+i], coords)
                coords.append([coord1[0]-i, coord1[1]+i])

        elif coord1[0] < coord2[0] and coord1[1] > coord2[1]:
            for i in range(coord1[1]-coord2[1]+1):
                counter += check([coord1[0]+i, coord1[1]-i], coords)
                coords.append([coord1[0]+i, coord1[1]-i])

        elif coord1[0] < coord2[0] and coord1[1] < coord2[1]:
            for i in range(coord2[0]-coord1[0]+1):
                counter += check([coord1[0]+i, coord1[1]+i], coords)
                coords.append([coord1[0]+i, coord1[1]+i])
        else:
            for i in range(coord1[0]-coord2[0]+1):
                counter += check([coord1[0]-i, coord1[1]-i], coords)
                coords.append([coord1[0]-i, coord1[1]-i])

    a = input().rstrip().split()

print(coords)
print(counter)