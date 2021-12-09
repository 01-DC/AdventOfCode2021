# full_input= open('test.txt').read().strip().split('\n')
full_input= open('input.txt').read().strip().split('\n')
display_outputs= []
for line in full_input:
    display_outputs.append(line[line.index('|')+1:].split())
ans= 0
for output in display_outputs:
    for segment in output:
        ans+= 1 if len(segment)!=5 and len(segment)!=6 else 0
print(ans)