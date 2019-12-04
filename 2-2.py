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

#get the ribbon size. Gonna be 2*small side + 2*med side + small*med*large.
def getRibbon(present):
    sides = []
    sides.append(present[0]*present[1])
    sides.append(present[0]*present[2])
    sides.append(present[1]*present[2])
    sides.sort()
    return 2*present[0] + 2*present[1] + present[0]*present[1]*present[2]

for line in fin:
    presents.append(getDimensions(line))

totalRibbon = 0

for box in presents:
    print(box, "has ribbon", getRibbon(box))
    totalRibbon += getRibbon(box)
    print("Total Ribbon now " + str(totalRibbon))

print(totalRibbon)
