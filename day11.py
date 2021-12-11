def check(grid):
    temp = grid[0][0]
    for j in range(len(grid)):
        for k in range(len(grid)):
            if grid[j][k]!= temp:
                return 0
    return 1
def flash(j, k, grid, total, checked):
    total.append(1)
    if k + 1 <= len(grid)-1:
        if checked[j][k+1] is False:
            grid[j][k+1] += 1
            if grid[j][k+1] > 9:
                grid[j][k + 1] = 0
                checked[j][k+1] = True
                flash(j, k+1, grid, total, checked)


        if j + 1 <= len(grid)-1:
            if checked[j + 1][k + 1] is False:
                grid[j + 1][k + 1] += 1
                if grid[j + 1][k+1] > 9:
                    grid[j + 1][k + 1] = 0
                    checked[j + 1][k + 1] = True
                    flash(j + 1, k+1, grid, total, checked)


        if j - 1 >= 0:
            if checked[j - 1][k + 1] is False:
                grid[j - 1][k + 1] += 1
                if grid[j - 1][k + 1] > 9:
                    grid[j - 1][k + 1] = 0
                    checked[j-1][k + 1] = True
                    flash(j - 1, k + 1, grid, total, checked)

    if k - 1 >= 0:
        if checked[j][k - 1] is False:
            grid[j][k - 1] += 1
            if grid[j][k - 1] > 9:
                grid[j][k - 1] = 0
                checked[j][k - 1] = True
                flash(j, k - 1, grid, total, checked)


        if j + 1 <= len(grid)-1:
            if checked[j + 1][k - 1] is False:
                grid[j + 1][k - 1] += 1
                if grid[j + 1][k-1] > 9:
                    grid[j + 1][k - 1] = 0
                    checked[j+1][k - 1] = True
                    flash(j + 1, k-1, grid, total, checked)

        if j - 1 >= 0:
            if checked[j - 1][k - 1] is False:
                grid[j - 1][k - 1] += 1
                if grid[j - 1][k-1] > 9:
                    grid[j - 1][k - 1] = 0
                    checked[j - 1][k - 1] = True
                    flash(j - 1, k-1, grid, total, checked)

    if j + 1 <= len(grid)-1:
        if checked[j+1][k] is False:
            grid[j + 1][k] += 1
            if grid[j+1][k] > 9:
                grid[j + 1][k] = 0
                checked[j + 1][k] = True
                flash(j+1, k, grid, total, checked)

    if j - 1 >= 0:
        if checked[j-1][k] is False:
            grid[j - 1][k] += 1
            if grid[j-1][k] > 9:
                grid[j - 1][k] = 0
                checked[j - 1][k] = True
                flash(j-1, k, grid, total, checked)


total = []
grid = []
for i in range(10):
    a = int(input())
    a = [int(a) for a in str(a)]
    grid.append(a)

for i in range(10000):
    if check(grid) == 1:
        print(i)
    for j in range(len(grid)):
        for k in range(len(grid)):
            grid[j][k] += 1
    checked = []
    for i in range(len(grid)):
        checked.append([False] * (len(grid)))
    for j in range(len(grid)):
        for k in range(len(grid)):
            if grid[j][k] > 9:
                grid[j][k] = 0
                checked[j][k] = True
                flash(j, k, grid, total, checked)


print(len(total))
print(grid)
