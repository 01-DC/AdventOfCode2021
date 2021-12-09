# full_input= open('test.txt').read().strip().split()
full_input= open('input.txt').read().strip().split()
heatmap= []
for line in full_input:
    heatmap.append(list(map(int, list(line))))

ROWS= len(heatmap)
COLUMNS= len(heatmap[0])
directions= [(1,0), (0,1), (-1,0), (0,-1)]
low_points= []

for r in range(ROWS):
    for c in range(COLUMNS):
        min_val= float('inf')
        for dx,dy in directions:
            x,y = c+dx,r+dy
            if 0<=x<COLUMNS and 0<=y<ROWS:
                min_val= min(min_val, heatmap[y][x])
        
        if min_val > heatmap[r][c]:
            low_points.append(heatmap[r][c]+1)

print(sum(low_points))
