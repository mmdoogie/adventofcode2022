#!/bin/python3

from aocd import lines
import numpy

segments = []

for l in lines:
	pts = l.split(" -> ")
	for n in range(len(pts)-1):
		pt1 = [int(x) for x in pts[n].split(",")]
		pt2 = [int(x) for x in pts[n+1].split(",")]
		segments += [[pt1, pt2]]

minX = min([min(s[0][0], s[1][0]) for s in segments])
minY = min([min(s[0][1], s[1][1]) for s in segments])
maxX = max([max(s[0][0], s[1][0]) for s in segments])
maxY = max([max(s[0][1], s[1][1]) for s in segments])

grid = numpy.zeros((maxX+2, maxY+2))

for s in segments:
	if s[0][0] == s[1][0]:
		y1, y2 = s[0][1], s[1][1]
		if y1 > y2:
			y1, y2 = y2, y1
		for y in range(y1, y2+1):
			grid[s[0][0],y] = 8
	else:
		x1, x2 = s[0][0], s[1][0]
		if x1 > x2:
			x1, x2 = x2, x1
		for x in range(x1, x2+1):
			grid[x,s[0][1]] = 8

def printGrid(grid):
	global sandPt
	print("---")
	for y in range(0, maxY+1):
		l = ""
		for x in range(minX, maxX+1):
			if sandPt[0] == x and sandPt[1] == y:
				l += "^"
			elif grid[x,y]==0:
				l += "."
			elif grid[x,y]==8:
				l += "#"
			else:
				l += "o"
		print(l)

escaped = False
particles = 0
while not escaped:
	sandPt = [500, 0]
	escaped = False

	while True:
		if grid[sandPt[0], sandPt[1]+1] == 0:
			sandPt = [sandPt[0], sandPt[1]+1]
			if sandPt[0] < minX or sandPt[0] > maxX or sandPt[1] > maxY:
				escaped = True
				break
		elif grid[sandPt[0]-1, sandPt[1]+1] == 0:
			sandPt = [sandPt[0]-1, sandPt[1]+1]
			if sandPt[0] < minX or sandPt[0] > maxX or sandPt[1] > maxY:
				escaped = True
				break
		elif grid[sandPt[0]+1, sandPt[1]+1] == 0:
			sandPt = [sandPt[0]+1, sandPt[1]+1]
			if sandPt[0] < minX or sandPt[0] > maxX or sandPt[1] > maxY:
				escaped = True
				break
		else:
			grid[sandPt[0], sandPt[1]] = 1
			particles += 1
			break

printGrid(grid)
print(particles)
			
