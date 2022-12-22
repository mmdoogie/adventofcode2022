#!/bin/python3

from aocd import lines
import re

grid = lines[0:-2]
instr = lines[-1]

rx = re.compile("([0-9]+)([LR])?")
steps = rx.findall(instr)

gwidth = max([len(g) for g in grid])
grid = [str.ljust(g, gwidth, " ") for g in grid]

gleft = []
gright = []
gtop = [1000]*gwidth
gbot = [0]*gwidth
for y,g in enumerate(grid):
	if "#" not in g:
		gleft += [g.index(".")]
		gright += [g.rindex(".")]
	else:
		gleft += [min(g.index("."), g.index("#"))]
		gright += [max(g.rindex("."), g.rindex("#"))]
	for n in range(gleft[y],gright[y]+1):
		if y < gtop[n]:
			gtop[n] = y
		if y > gbot[n]:
			gbot[n] = y

pos = [gleft[0], 0]
hdgs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
face = [">", "v", "<", "^"]
hidx = 0

for s in steps:
	for n in range(int(s[0])):
		np = [pos[0] + hdgs[hidx][0], pos[1] + hdgs[hidx][1]]
		if hdgs[hidx][0] != 0:
			if np[0] > gright[np[1]]:
				np[0] = gleft[np[1]]
			if np[0] < gleft[np[1]]:
				np[0] = gright[np[1]]
		else:
			if np[1] > gbot[np[0]]:
				np[1] = gtop[np[0]]
			if np[1] < gtop[np[0]]:
				np[1] = gbot[np[0]]
		npc = grid[np[1]][np[0]]
		assert npc != " "
		if npc == "#":
			break
		pos = np
		assert grid[pos[1]][pos[0]] != "#"
		gs = [*grid[pos[1]]]
		gs[pos[0]] = face[hidx]
		grid[pos[1]] = ''.join(gs)
	if s[1] == "R":
		hidx += 1
		if hidx > 3:
			hidx = 0
	elif s[1] == "L":
		hidx -= 1
		if hidx < 0:
			hidx = 3

print("Final Pos:", pos, "Heading:", hidx, face[hidx])
print("Code:", 1000*(pos[1]+1) + 4*(pos[0]+1) + hidx)

#for g in grid:
#	print(g)
