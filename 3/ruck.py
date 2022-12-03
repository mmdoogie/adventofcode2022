#!/bin/python3

def priority(item):
	if item >= 'a' and item <= 'z':
		return ord(item)-ord('a')+1
	if item >= 'A' and item <= 'Z':
		return ord(item)-ord('A')+27
	print("PANIC!")

with open("input", mode="r") as file:
	score = 0
	for l in file:
		gotmatch = 0
		s=len(l)-1
		p=int(s/2)

		gotmatch = (set(l[0:p]) & set(l[p:s])).pop()

		print(gotmatch)
		score += priority(gotmatch)

	print(score)
