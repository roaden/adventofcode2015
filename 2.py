#grab my input

fin = open('input2.txt', 'r')

presents = []

def getDimensions(foo):
    foo = foo.strip('\n')
    foo = foo.split('x')
    present = []
    for i in range(len(foo)):
        present.append(int(foo[i]))
    return present

#get the dimensions. Should be 3*smallest side + 2* each other side's area.
def getPaper(present):
    sides = []
    sides.append(present[0]*present[1])
    sides.append(present[0]*present[2])
    sides.append(present[1]*present[2])
    sides.sort()
    return 3*sides[0] + 2*sides[1] + 2*sides[2] 

for line in fin:
    presents.append(getDimensions(line))

totalPaper = 0

for box in presents:
    totalPaper += getPaper(box)

print(totalPaper)
