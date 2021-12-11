a = input()
b = []
total = 0
while a != 'n':
    b.append(a)
    a = input()

for i in range(len(b)):
    for j in range(len(b[0])):
        if j+1 > len(b[0])-1 or int(b[i][j]) < int(b[i][j+1]):
            if j-1 < 0 or int(b[i][j]) < int(b[i][j-1]):
                if i + 1 > len(b) - 1 or int(b[i][j]) < int(b[i+1][j]):
                    if i-1 < 0 or int(b[i][j]) < int(b[i-1][j]):
                        total += int(b[i][j]) + 1

print(total)