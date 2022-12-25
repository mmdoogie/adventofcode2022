#!/bin/python3

from aocd import lines
import math

symToDigits = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
digitsToSym = {v: k for k, v in symToDigits.items()}

def fromBaseWeird(s):
	global symToDigits
	n = 0
	x = 0
	for d in reversed(list(s)):
		n += symToDigits[d] * 5 ** x
		x += 1
	return n

tot = 0
for l in lines:
	tot += fromBaseWeird(l)

print(tot)

def toBaseWeird(n):
	x = math.floor(math.log(n, 5))
	s = [0] * (x + 1)
	for o in range(x, -1, -1):
		exa = 5 ** o
		d = int(round(n / exa, 0))
		n -= d * exa
		s[o] = d
		o -= 1
	return ''.join([digitsToSym[d] for d in reversed(s)])

print(toBaseWeird(tot))
