a = str(input())
b = []

while a != 'n':
    b.append(a)
    a = str(input())

oxygen = ''
co2 = ''
removed = 0
print(b)
for i in range(len(b[0])):
    temp1 = 0
    temp2 = 0
    if len(b) == 1:
        break
    for j in range(len(b)):

        if b[j][i] == '0':
            temp1 += 1
        else:
            temp2 += 1

    if temp1 <= temp2:
        for k in range(len(b)-1, -1, -1):
            if b[k][i] == '0':
                b.pop(k)
    else:
        for k in range(len(b)-1, -1, -1):
            if b[k][i] == '1':
                b.pop(k)

print(b)
