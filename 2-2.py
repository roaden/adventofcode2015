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
    sides = present
    sides.sort()
    return 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]

for line in fin:
    presents.append(getDimensions(line))

totalRibbon = 0

for box in presents:
    print(box, "has ribbon", getRibbon(box))
    totalRibbon += getRibbon(box)
    print("Total Ribbon now " + str(totalRibbon))

print(totalRibbon)
