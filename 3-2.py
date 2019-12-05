#Get the input
fin = open('input3.txt' , 'r')

dirs = fin.readline().strip('\n')

xsanta = 0
ysanta = 0
xbot = 0
ybot = 0
santasturn = True

visited = ['0,0']
for i in dirs:
    if i == '<':
        if santasturn:
            xsanta -= 1
        else:
            xbot -= 1
    elif i == '>':
        if santasturn:
            xsanta += 1
        else:
            xbot += 1
    elif i == 'v':
        if santasturn:
            ysanta -= 1
        else:
            ybot -= 1
    elif i == '^':
        if santasturn:
            ysanta += 1
        else:
            ybot += 1
    else:
        print('Unexpected character: ' + i + '  Exiting.')
        break
    if santasturn:
        visited.append(str(xsanta) + ',' + str(ysanta))
    else:
        visited.append(str(xbot) + ',' + str(ybot))
    santasturn = not santasturn

visited = list(set(visited))
print(len(visited))
