#!/bin/python3

from aocd import lines
import functools

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

for m in range(len(allLines)):
	for n in range(len(allLines)-m-1):
		if not cmp(allLines[n], allLines[n+1]):
			allLines[n+1], allLines[n] = allLines[n], allLines[n+1]

print((allLines.index(key1)+1) * (allLines.index(key2)+1))
