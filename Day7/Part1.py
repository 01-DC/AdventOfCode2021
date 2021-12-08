import statistics
# positions= list(map(int, open('test.txt').read().strip().split(',')))
positions= list(map(int, open('input.txt').read().strip().split(',')))
min_position= int(statistics.median(positions))
ans= 0
for position in positions:
    ans+= abs(position-min_position)
print(ans)