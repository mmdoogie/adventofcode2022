#!/bin/python3

from aocd import lines

regX = 1
valHist = []

for l in lines:
	p = l.split(" ")
	if p[0] == "noop":
		valHist += [regX]
	if p[0] == "addx":
		valHist += [regX]
		valHist += [regX]
		regX += int(p[1])

print(sum([n * valHist[n-1] for n in range(20, len(valHist), 40)]))

for y in range(6):
	line = ""
	for x in range(40):
		sc = valHist[40*y + x]
		if abs(x - sc) <= 1:
			line += "@"
		else:
			line += " "
	print(line)
