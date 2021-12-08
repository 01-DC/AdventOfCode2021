# full_input= open("test.txt").read().strip().split('\n')
# matrix= [[0 for c in range(10)] for r in range(10)]
full_input= open("input.txt").read().strip().split('\n')
matrix= [[0 for c in range(990)] for r in range(991)]
for each_input in full_input:
    p1, p2= each_input.split(' -> ')
    x1, y1= list(map(int, p1.split(',')))
    x2, y2= list(map(int, p2.split(',')))
    if x1==x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            matrix[y][x1]+= 1
    elif y1==y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            matrix[y1][x]+= 1
    # print(p1 + ' ' + p2)
# print(matrix)
ans= 0
for r in matrix:
    for c in r:
        if c > 1:
            ans+= 1
print(ans)