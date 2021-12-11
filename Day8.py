a = input().split('|')
b = a[0].split()
c = a[1].split()
d = b + c
count = 0
number = ['']*7
answer1 = 0
two = ''
three = ''
four = ''
five = ''
five2 = ''
six2 = ''
six = ''
seven = ''
while a != ['n']:
    two = ''
    three = ''
    four = ''
    five = ''
    five2 = ''
    six2 = ''
    six = ''
    seven = ''
    for i in range(len(b)):

        if len(b[i]) == 2:
            two = b[i]
        if len(b[i]) == 3:
            three = b[i]
        if len(b[i]) == 4:
            four = b[i]
        if len(b[i]) == 5:
            five += b[i]
        if len(b[i]) == 6:
            six += b[i]
        if len(b[i]) == 7:
            seven = b[i]
    for i in range(len(five)):
        temp = five.count(five[i])
        if temp == 1:
            five2 += five[i]
    for i in range(len(six)):
        temp = six.count(six[i])
        if temp == 2:
            if six[i] not in six2:
                six2 += six[i]

    for i in range(3):
        if three[i] not in two:
            number[0] = three[i]
    for i in range(3):
        if six2[i] in two:
            number[2] = six2[i]
            if two[0] == six2[i]:
                number[5] = two[1]
            else:
                number[5] = two[0]
    for i in range(2):
        if five2[i] in four:
            number[1] = five2[i]
        else:
            number[4] = five2[i]


    for i in range(4):
        if four[i] not in five2 + two:
            number[3] = four[i]

    for i in range(7):
        if seven[i] not in number:
            number[6] = seven[i]
    number2 = ['']*10
    number2[0] = number[0] + number[1] + number[2] + number[4] + number[6] + number[5]
    number2[1] = number[2] + number[5]
    number2[2]= number[0]+number[2]+number[3]+number[4]+number[6]
    number2[3]= number[0] + number[2] + number[3] + number[5] + number[6]
    number2[4]= number[1] + number[2] + number[3] + number[5]
    number2[5]= number[0] + number[1] + number[3] + number[5] + number[6]
    number2[6]= number[0] + number[1] + number[3] + number[4] + number[6] + number[5]
    number2[7]= number[0]+number[2]+number[5]
    number2[8]= number[0] + number[1] + number[3] + number[4] + number[6] + number[5] + number[2]
    number2[9]= number[0] + number[1] + number[2] + number[3] + number[6] + number[5]
    for i in range(len(number2)):
        number2[i] = "".join(sorted(number2[i]))

    answer = []
    for i in range(len(c)):
        for j in range(len(number2)):
            c[i] = "".join(sorted(c[i]))
            if c[i] == number2[j]:
                answer.append(j)

    answer1 += (answer[0]*1000 + answer[1]*100 + answer[2] * 10 + answer[3])

    a = input().rstrip().split('|')
    if a != ['n']:
        b = a[0].split()
        c = a[1].split()
        d = b + c

print(answer1)
