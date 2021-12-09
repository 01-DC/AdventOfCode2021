from statistics import mean
from math import ceil, floor

# positions= list(map(int, open('test.txt').read().strip().split(',')))
positions= list(map(int, open('input.txt').read().strip().split(',')))
# mean_pos= round(statistics.mean(positions))-1 # -1 was done based on testing sadge
# print(mean_pos)
mean_up= ceil(mean(positions))
mean_down= floor(mean(positions))

ans_up, ans_down= 0, 0
for position in positions:
    n_up, n_down= abs(position-mean_up), abs(position-mean_down)
    ans_up+= (n_up*(n_up+1))/2
    ans_down+= (n_down*(n_down+1))/2

print(min(ans_up, ans_down))