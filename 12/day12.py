#!/bin/python3

from aocd import lines

hmap = []

for n,l in enumerate(lines):
	h = [ord(x)-ord('a') for x in list(l)]
	hmap += [h]
	if -14 in h: #S
		startPos = (h.index(-14), n)
		h[h.index(-14)] = 0
	if -28 in h: #E
		endPos = (h.index(-28), n)
		h[h.index(-28)] = 25

nodePos = []
nodeDist = []
nodeVisited = []
for y in range(len(lines)):
	for x in range(len(lines[0])):
		nodePos += [(x,y)]
		nodeDist += [int(10e6)]
		nodeVisited += [False]

nodeDist[nodePos.index(startPos)] = 0

maxX = len(lines[0])-1
maxY = len(lines)-1
currPos = startPos

while True:
	neighbors = []
	if currPos[0] > 0:
		neighbors += [(currPos[0]-1, currPos[1])]
	if currPos[0] < maxX-1:
		neighbors += [(currPos[0]+1, currPos[1])]
	if currPos[1] > 0:
		neighbors += [(currPos[0], currPos[1]-1)]
	if currPos[1] < maxY-1:
		neighbors += [(currPos[0], currPos[1]+1)]

	for n in neighbors:
		if nodeVisited[nodePos.index(n)]:
			continue
		dh = hmap[n[1]][n[0]] - hmap[currPos[1]][currPos[0]]
		if dh <= 1:
			newDist = nodeDist[nodePos.index(currPos)] + 1
			if newDist < nodeDist[nodePos.index(n)]:
				nodeDist[nodePos.index(n)] = newDist

	nodeVisited[nodePos.index(currPos)] = True
	if currPos == endPos:
		break

	remDist = min([x for n,x in enumerate(nodeDist) if not nodeVisited[n]])
	if remDist == int(10e6):
		break

	currPos = [x for n,x in enumerate(nodePos) if not nodeVisited[n] and nodeDist[n] == remDist][0]

if currPos == endPos:
	print(nodeDist[nodePos.index(endPos)])
