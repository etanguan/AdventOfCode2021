def floodfill(b, i, j, area, searched):
    searched[i][j] = True
    area.append(1)
    if j + 1 <= len(b[0]) - 1 and searched[i][j+1] is False and b[i][j + 1] != '9':
        floodfill(b, i, j + 1, area, searched)

    if j-1 >= 0 and searched[i][j-1] is False and b[i][j - 1] != '9':
        floodfill(b, i, j - 1, area, searched)

    if i + 1 <= len(b) - 1 and searched[i+1][j] is False and b[i+1][j] != '9':
        floodfill(b, i+1, j, area, searched)

    if i-1 >= 0 and searched[i-1][j] is False and b[i-1][j] != '9':
        floodfill(b, i-1, j, area, searched)

a = input()
b = []
total = []
while a != 'n':
    b.append(a)
    a = input()

searched = []
for i in range(len(b)):
    searched.append([False]*len(b[0]))
for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] != '9':
            if searched[i][j] is False:
                area = []
                floodfill(b, i, j, area, searched)
                total.append(len(area))

c = 1
for i in range(3):
    c = c*max(total)
    total.remove(max(total))
print(c)