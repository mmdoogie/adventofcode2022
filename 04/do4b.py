#!/bin/python3

from functools import reduce

with open("input", mode="r") as file:
	lines = file.readlines()

containsCount = 0
overlapsCount = 0

for l in lines:
	left, right = l.strip().split(",")

	leftMin, leftMax = left.split("-")
	rightMin, rightMax = right.split("-")

	leftMin = int(leftMin)
	leftMax = int(leftMax)
	rightMin = int(rightMin)
	rightMax = int(rightMax)

	leftRange = range(leftMin, leftMax+1)
	rightRange = range(rightMin, rightMax+1)

	leftContains = all([x in rightRange for x in leftRange])
	rightContains = all([x in leftRange for x in rightRange])
	if leftContains or rightContains:
		containsCount += 1
	
	overlaps = any([x in rightRange for x in leftRange])
	if overlaps:
		overlapsCount += 1

print(containsCount)
print(overlapsCount)
