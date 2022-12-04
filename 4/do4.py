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

	if leftMin <= rightMin and leftMax >= rightMax:
		containsCount += 1
	elif rightMin <= leftMin and rightMax >= leftMax:
		containsCount += 1
	
	if leftMin >= rightMin and leftMin <= rightMax:
		overlapsCount += 1
	elif rightMin >= leftMin and rightMin <= leftMax:
		overlapsCount += 1

print(containsCount)
print(overlapsCount)
