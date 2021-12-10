# full_input= open('test.txt').read().strip().split('\n')
full_input= open('input.txt').read().strip().split('\n')
points= {')':3, ']':57, '}':1197, '>':25137}
braces= {')':'(', ']':'[', '}':'{', '>':'<'}
ans= 0
for line in full_input:
    stack= []
    for ch in list(line):
        if '([{<'.find(ch)>-1:
            stack.append(ch)
        else:
            temp= stack.pop()
            if braces[ch]==temp:
                continue
            ans+= points[ch]
            break

print(ans)