#!/bin/python3

from aocd import lines

signal = lines[0]

def findMarker(markerLen):
	for n in range(len(signal)):
		chars = signal[n:n+markerLen]
		if len(set(chars)) == markerLen:
			return n+markerLen

print(findMarker(4))
print(findMarker(14))
