#Find the floor

floor = 0

#get the input

fin = open('input1.txt', 'r')

theMap = fin.readline().strip('\n')

#( goes up, ) goes down

for i in theMap:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1

print(floor)
