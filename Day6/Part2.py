# fishes= list(map(int, open('test.txt').read().strip().split(',')))
fishes= list(map(int, open('input.txt').read().strip().split(',')))
for day in range(80):
    new_fishes= []
    for index, fish in enumerate(fishes):
        if fish==0:
            fishes[index]= 7
            new_fishes.append(8)
        fishes[index]-= 1
    fishes.extend(new_fishes)
    # print(day, fishes)
print(len(fishes))