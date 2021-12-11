a = input().rstrip().split(',')
a = [int(i) for i in a]
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
temp = [0]*9
for i in range(len(a)):
    lst[a[i]] += 1
    temp[a[i]] += 1
for i in range(9999999):

    lst[7] = temp[8]
    lst[6] = temp[7]
    lst[5] = temp[6]
    lst[4] = temp[5]
    lst[3] = temp[4]
    lst[2] = temp[3]
    lst[1] = temp[2]
    lst[0] = temp[1]
    lst[8] = temp[0]
    lst[6] += temp[0]
    temp = lst.copy()


print(sum(lst))
