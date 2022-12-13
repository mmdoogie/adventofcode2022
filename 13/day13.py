#!/bin/python3

from aocd import lines
from functools import cmp_to_key

def cmp(left, right):
	for n in range(len(left)):
		if n > len(right)-1:
			return False

		if isinstance(left[n], int) and isinstance(right[n], int):
			if left[n] != right[n]:
				return left[n] < right[n]
			else:
				continue
		elif isinstance(left[n], list) and isinstance(right[n], list):
			c = cmp(left[n], right[n])
			if c != None:
				return c
			else:
				continue
		elif isinstance(left[n], list) and isinstance(right[n], int):
			c = cmp(left[n], [right[n]])
			if c != None:
				return c
			else:
				continue
		elif isinstance(left[n], int) and isinstance(right[n], list):
			c = cmp([left[n]], right[n])
			if c != None:
				return c
			else:
				continue
		else:
			print("PANIC")

	if len(left) < len(right):
		return True
	else:
		return None

correct = []		
for n in range(0, len(lines), 3):
	ll = eval(lines[n])
	rl = eval(lines[n+1])
	c = cmp(ll, rl)
	
	if c:
		correct += [n]

print(sum([c//3 + 1 for c in correct]))

allLines = [eval(l) for l in lines if len(l) != 0]
key1, key2 = [[2]], [[6]]
allLines += [key1, key2]

fixit = {True: -1, None: 0, False: 1}
allLines.sort(key=cmp_to_key(lambda l,r:fixit[cmp(l,r)]))

print((allLines.index(key1)+1) * (allLines.index(key2)+1))
