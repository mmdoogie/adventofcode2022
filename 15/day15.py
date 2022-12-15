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
xmax = max(max([s[0] for s in sources]), max([b[0] for b in beacons]))

cover = []
for n,s in enumerate(sources):
	sbd = mdis(s,beacons[n])
	dy = int(abs(s[1] - LINE))
	dx = sbd - dy

	if dy > sbd:
		continue

	cover += [(s[0]-dx, s[0]+dx)]

cover.sort(key=lambda x:x[0])
xl, xr = cover[0]

nogo = 0
for c in cover:
	if c[0] >= xl and c[0] <= xr:
		if c[1] <= xr:
			continue
		else:
			xr = c[1]
	else:
		nogo = xr - xl
		xl, xr = c

nogo += xr - xl

print(nogo)
