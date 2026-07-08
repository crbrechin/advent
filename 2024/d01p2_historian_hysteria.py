from collections import defaultdict

ledger = open("d01_historian_hysteria.txt")

historian1 = []
historian2 = []

frequency = defaultdict(int)

similarity = 0

for line in ledger.readlines():
    l = line.split()
    # print(f'{l}') # DEBUG
    historian1.append(int(l[0]))
    historian2.append(int(l[1]))
    
for h in historian1:
    frequency[h] = historian2.count(h)
    
# print(f'{frequency}\n') # DEBUG
    
for f in frequency:
    similarity += frequency[f] * f

print(f'{similarity}') # DEBUG
