ledger = open("d01_historian_hysteria.txt")

historian1 = []
historian2 = []

difference = 0

for line in ledger.readlines():
    l = line.split()
    # print(f'{l}') # DEBUG
    historian1.append(int(l[0]))
    historian2.append(int(l[1]))

i,n = 0,len(historian1)

while i < n:
    
    d1 = historian1.pop(historian1.index(min(historian1)))
    d2 = historian2.pop(historian2.index(min(historian2)))

    
    difference += abs(d1 - d2)
    
    i += 1

print(f'{difference}') # DEBUG
