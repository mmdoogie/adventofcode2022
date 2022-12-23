#!/bin/python3

from aocd import lines
from collections import Counter
from collections import deque

elves = {}

for y,l in enumerate(lines):
	for x,c in enumerate(l):
		if c == "#":
			elves[(x,y)] = True

dirList = deque(["N", "S", "W", "E"])
dirOff = {"N": (0, -1), "S": (0, 1), "W": (-1, 0), "E": (1,0)}

rounds = 0
changed = 1
while changed:
	rounds += 1
	changed = 0
	proposal = []
	for e,_ in elves.items():
		np = []
		for d in dirList:
			dx, dy = dirOff[d]
			ok = True
			if d in "NS":
				for ddx in range(-1,2):
					if (e[0]+ddx, e[1]+dy) in elves:
						ok = False
			else:
				for ddy in range(-1,2):
					if (e[0]+dx, e[1]+ddy) in elves:
						ok = False
			if ok:
				np += [(e[0]+dx, e[1]+dy)]
		
		if len(np) == 4 or len(np) == 0:
			proposal += [None]
		else:
			proposal += [np[0]]

	assert len(elves) == len(proposal)
	
	src = list(elves.keys())
	cnt = Counter(proposal)

	for n,p in enumerate(proposal):
		if cnt[p] == 1:
			del elves[src[n]]
			elves[p] = True
			changed += 1

	if (rounds % 25 == 0):
		print(rounds, changed)
	
	dirList.rotate(-1)

print(rounds)
