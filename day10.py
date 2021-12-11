a = input()
opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
auto = []
total = 0
while a != 'n':
    total = 0
    lst = []
    for i in range(len(a)):
        if a[i] in opening:
            lst.append(a[i])
        else:
            if lst[len(lst)-1] == opening[closing.index(a[i])]:
                lst.pop(len(lst)-1)
            else:
                if a[i] == ')':
                    total += 3
                if a[i] == ']':
                    total += 57
                if a[i] == '}':
                    total += 1197
                if a[i] == '>':
                    total += 25137
    if total == 0:
        temp = 0
        for i in range(len(lst)-1, -1, -1):
            temp = temp * 5
            if lst[i] == '(':
                temp += 1
            if lst[i] == '[':
                temp += 2
            if lst[i] == '{':
                temp += 3
            if lst[i] == '<':
                temp += 4
        auto.append(temp)

    a = input()

auto.sort()

print(auto[(len(auto)-1)//2])
