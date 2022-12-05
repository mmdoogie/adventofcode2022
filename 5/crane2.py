#!/bin/python3

with open("input", mode="r") as file:
	lines = file.readlines()

header = lines[0:8]
moves = lines[10:]

stacks = [[],[],[],[],[],[],[],[],[]]
for l in header:
	for c in range(0, 9):
		x = l[1 + 4*c]
		if x != ' ':
			stacks[c] = [x] + stacks[c]

def printStacks(s):
	print([''.join(x) for x in s])

for m in moves:
	parts = m.strip().split(" ")
	qty = int(parts[1])
	src = int(parts[3])-1
	dst = int(parts[5])-1

	printStacks(stacks)
	print(m.strip())
	stacks[dst] = stacks[dst] + stacks[src][-qty:]
	stacks[src] = stacks[src][0:-qty]
	printStacks(stacks)
	print()

result = ''.join([s[-1] for s in stacks])
print(result)
