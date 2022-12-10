#!/bin/python3

def priority(item):
	if item >= 'a' and item <= 'z':
		return ord(item)-ord('a')+1
	if item >= 'A' and item <= 'Z':
		return ord(item)-ord('A')+27

with open("input", mode="r") as file:
	score = 0

	group = []
	c = 0
	for l in file:
		group.append(l.strip())
		c = c + 1
		if c == 3:
			gotmatch = (set(group[0]) & set(group[1]) & set(group[2])).pop()
			group = []
			c = 0

			print(gotmatch)
			score += priority(gotmatch)
	
	print(score)
