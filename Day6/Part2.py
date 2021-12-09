# starting_input= list(map(int, open('test.txt').read().strip().split(',')))
starting_input= list(map(int, open('input.txt').read().strip().split(',')))
current_fishes= [0 for i in range(9)]
for fish in starting_input:
    current_fishes[fish]+= 1

for day in range(256):
    dead_fishes= current_fishes[0]
    # for i in range(8):
    #     current_fishes[i]= current_fishes[i+1]
    current_fishes= [current_fishes[i+1] for i in range(8)]
    current_fishes.append(0)
    current_fishes[6]+= dead_fishes
    current_fishes[8]= dead_fishes
print(sum(current_fishes))

