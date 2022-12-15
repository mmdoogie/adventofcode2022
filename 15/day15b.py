#!/bin/python3

from aocd import lines
#with open("ex", mode="r") as f:
#	lines = [l.strip() for l in f.readlines()]

LIMIT=4000000

def mdis(a, b):
	return round(abs(a[0]-b[0])+abs(a[1]-b[1]), 0)

sources = []
beacons = []
sbds = []
for l in lines:
	p = l.split(":")
	v = p[0].split(", ")
	s = (int(v[0].split("=")[1]), int(v[1].split("=")[1]))
	v = p[1].split(",")
	b = (int(v[0].split("=")[1]), int(v[1].split("=")[1]))
	sources += [s]
	beacons += [b]
	sbds += [mdis(s,b)]

for y in range(0, LIMIT+1):
	cover = []
	for n,s in enumerate(sources):
		sbd = sbds[n]
		
		dy = int(abs(s[1] - y))
		if dy > sbd:
			continue
		
		dx = sbd - dy
		x1 = max(0, s[0]-dx)
		x2 = min(LIMIT, s[0]+dx)
		cover += [(x1, x2)]
	
	cover.sort(key=lambda x:x[0])

	if y % 100000 == 0:
		print(y)

	if cover[0][0] >= 2:
		continue
	
	xl, xr = cover[0]
	
	cand = 0
	candx = []
	for c in cover:
		if c[0] >= xl and c[0] <= xr:
			if c[1] <= xr:
				continue
			else:
				xr = c[1]
		else:
			if c[0]-xr == 2:
				cand += 1
				candx += [xr+1]
			xl, xr = c

	if LIMIT - xr == 1:
		cand += 1
		candx += [LIMIT]
	elif LIMIT - xr != 0:
		cand = 0

	if cand == 1:
		print(f"x={candx[0]}, y={y}, freq={4000000*candx[0]+y}")
		break

