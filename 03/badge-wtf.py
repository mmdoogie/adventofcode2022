#!/bin/python3

from functools import reduce

with open("input", mode="r") as file:
	lines = file.readlines()

score = sum(map(lambda f:ord(f)-ord('a')+1 if f>='a' else ord(f)-ord('A')+27, [reduce(lambda a,b:a&b, [set(y.strip()) for y in x]).pop() for x in [lines[n-2:n+1] for n in range(len(lines)) if n%3==2]]))

print(score)
