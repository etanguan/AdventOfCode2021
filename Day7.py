a = input().rstrip().split(',')
a = [int(i) for i in a]

n = max(a)
lst = []
for i in range(n):
    temp = 0
    extra = 0
    for j in range(len(a)):
        temp += (abs(a[j]-i)/2) * (abs(a[j]-i)+1)
    lst.append(temp)
print(min(lst))