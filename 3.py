#Get the input
fin = open('input3.txt' , 'r')

dirs = fin.readline().strip('\n')

x = 0
y = 0

visited = ['0,0']
for i in dirs:
    if i == '<':
        x -= 1
    elif i == '>':
        x += 1
    elif i == 'v':
        y -= 1
    elif i == '^':
        y += 1
    else:
        print('Unexpected character: ' + i + '  Exiting.')
        break
    visited.append(str(x) + ',' + str(y))

visited = list(set(visited))
print(len(visited))
