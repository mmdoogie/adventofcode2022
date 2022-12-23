#!/bin/python3

from aocd import lines
from collections import Counter
from collections import deque

elves = {}

for y, l in enumerate(lines):
	for x, c in enumerate(l):
		if c == "#":
			elves[(x, y)] = True

dirList = deque(["N", "S", "W", "E"])
dirOff = {"N": (0, -1), "S": (0, 1), "W": (-1, 0), "E": (1,0)}

for r in range(0, 10):
	proposal = []
	for e in elves:
		np = []
		for d in dirList:
			dx, dy = dirOff[d]
			ok = True
			if d in "NS":
				for ddx in range(-1, 2):
					if (e[0] + ddx, e[1] + dy) in elves:
						ok = False
			else:
				for ddy in range(-1, 2):
					if (e[0] + dx, e[1] + ddy) in elves:
						ok = False
			if ok:
				np += [(e[0] + dx, e[1] + dy)]
		
		if len(np) == 4 or len(np) == 0:
			proposal += [None]
		else:
			proposal += [np[0]]

	assert len(elves) == len(proposal)

	src = list(elves.keys())
	cnt = Counter(proposal)

	for n, p in enumerate(proposal):
		if cnt[p] == 1:
			del elves[src[n]]
			elves[p] = True

	dirList.rotate(-1)

minX = min([e[0] for e in elves])
maxX = max([e[0] for e in elves])
minY = min([e[1] for e in elves])
maxY = max([e[1] for e in elves])

a = (maxX - minX + 1) * (maxY - minY + 1)
print("X:", minX, "to", maxX, "Y:", minY, "to", maxY)
print("Area", a)
print("Elves", len(elves))
print("Free", a - len(elves))
