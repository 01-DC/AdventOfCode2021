# full_input= open("test.txt").read().strip().split('\n')
full_input= open("input.txt").read().strip().split('\n')
draw_order= full_input[0].split(',')
matrices= [[line.split() for line in full_input[pos:pos+5]] for pos in range(2, len(full_input), 6)]

def mark(matrix, number):
    for r in range(5):
        for c in range(5):
            if matrix[r][c]==number:
                matrix[r][c]= 'X'
                return matrix
    return matrix

def checkBingo(matrix):
    for r in matrix:
        if r.count('X')==5:
            return True
        
    for x in range(5):
        if([r[x] for r in matrix].count('X')==5):
            return True
    
    return False

def calcSum(matrix):
    return sum([sum([int(num) for num in row if num!='X']) for row in matrix])

for draw in draw_order:
    for matrix in matrices:
        matrix= mark(matrix, draw)
        # print(matrix)
        if(checkBingo(matrix)):
            unmarked_sum= calcSum(matrix)
            print(unmarked_sum*int(draw))
            exit()
