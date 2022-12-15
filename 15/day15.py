#!/bin/python3

from aocd import lines
LINE=2000000

sources = []
beacons = []
for l in lines:
	p = l.split(":")
	v = p[0].split(", ")
	s = (int(v[0].split("=")[1]), int(v[1].split("=")[1]))
	v = p[1].split(",")
	b = (int(v[0].split("=")[1]), int(v[1].split("=")[1]))
	sources += [s]
	beacons += [b]

def mdis(a, b):
	return round(abs(a[0]-b[0])+abs(a[1]-b[1]), 0)

xmin = min(min([s[0] for s in sources]), min([b[0] for b in beacons]))
ymin = min(min([s[1] for s in sources]), min([b[1] for b in beacons]))
xmax = max(max([s[0] for s in sources]), max([b[0] for b in beacons]))
ymax = max(max([s[1] for s in sources]), max([b[1] for b in beacons]))

xp = list(range(xmin, xmax+1))

xrow = [0 for x in xp]
lxp = len(xp)

extra = 0
for n,s in enumerate(sources):
	sbd = mdis(s,beacons[n])
	dy = int(abs(s[1] - LINE))
	dx = sbd - dy

	if dy > sbd:
		continue

	xs = s[0]-dx
	xi = xp.index(xs)

	ex = 0
	for x in range(0, 2*dx+1):
		if xi+x < lxp-1:
			xrow[xi+x] = 1
		else:
			ex += 1
	if ex > extra:
		extra = ex

bir = 0
for b in set(beacons):
	if b[1] == LINE:
		bir += 1

print(f"{sum(xrow)} - {bir} + {extra} = {sum(xrow)-bir+extra}")
