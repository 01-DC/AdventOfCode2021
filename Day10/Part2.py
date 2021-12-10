# full_input= open('test.txt').read().strip().split('\n')
full_input= open('input.txt').read().strip().split('\n')
points= {')':1, ']':2, '}':3, '>':4}
braces= {'(':')', '[':']', '{':'}', '<':'>'}
total_score= []
for line in full_input:
    stack= []
    line_score= 0
    for ch in list(line):
        if '([{<'.find(ch)>-1:
            stack.append(braces[ch])
        elif ch!=stack[-1]:
            stack.clear()
            break
        else:
            stack.pop()
    for ch in stack[::-1]:
        line_score= (line_score*5)+ points[ch]
    if line_score!=0:
        total_score.append(line_score)
total_score.sort()
print(total_score[len(total_score)//2])