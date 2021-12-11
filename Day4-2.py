draws = input().split(',')
draws = [int(a) for a in draws]

a = input().rstrip().split()

winner = 0
lastnum = 0
boardr = []
boardc = []
tempr = 0
tempc = 0
counter = -1
while a != ['n']:
    if a == []:

        boardr.append(tempr)
        boardc.append(tempc)
        tempr = []
        tempc = [[],[],[],[],[]]
        counter += 1

    else:
        tempr.append(a)
        for i in range(len(a)):
            tempc[i].append(a[i])
    a = input().rstrip().split()
    if a != ['n']:
        a = [int(i) for i in a]

check = [False] * (len(boardr) + 1)
wincount = 0
boardr.append(tempr)
boardc.append(tempc)
boardr.pop(0)
boardc.pop(0)
for i in range(len(draws)):
    for j in range(len(boardr)):
        for k in range(len(boardr[j])):
            for l in range(len(boardr[j][k])-1, -1, -1):
                if boardr[j][k][l] == draws[i]:
                    if wincount != len(boardr):
                        boardr[j][k].pop(l)
                        if len(boardr[j][k]) == 0:
                            if check[j] is False:

                                if wincount != len(boardr):

                                    wincount += 1
                                    winner = j
                                    lastnum = draws[i]
                                    check[j] = True


    for j in range(len(boardc)):
        for k in range(len(boardc[j])):
            for l in range(len(boardc[j][k])-1, -1, -1):
                if boardc[j][k][l] == draws[i]:
                    if wincount != len(boardr):
                        boardc[j][k].pop(l)
                        if len(boardc[j][k]) == 0:
                            if check[j] is False:
                                if wincount != len(boardr):

                                    wincount += 1
                                    winner = j
                                    lastnum = draws[i]
                                    check[j] = True

counter = 0
for i in range(len(boardc[winner])):
    for j in boardc[winner][i]:
        counter += j

print(winner)
print(counter*lastnum)
print(counter)
print(lastnum)

