#Find the floor

floor = 0

#get the input

fin = open('input1.txt', 'r')

theMap = fin.readline().strip('\n')

#( goes up, ) goes down

for i in range(len(theMap)):
    if theMap[i] == '(':
        floor += 1
    elif theMap[i] == ')':
        floor -= 1
    if floor < 0:
        print("Yer in the basement, 'arry, after " + str(i+1) + " steps.")
        break

