#!/bin/python3

from aocd import lines

monkeys = {}
for l in lines:
	p = l.split(": ")
	name = p[0]
	if p[1].isnumeric():
		op = "yell"
		nl = None
		nr = None
		val = int(p[1])
	else:
		s = p[1].split(" ")
		nl = s[0]
		op = s[1]
		nr = s[2]
		val = None
	monkeys[name] = {"op": op, "nl": nl, "nr": nr, "val": val}

while not monkeys["root"]["val"]:
	for n,m in monkeys.items():
		if m["val"]:
			continue
		if monkeys[m["nl"]]["val"] and monkeys[m["nr"]]["val"]:
			os = str(monkeys[m["nl"]]["val"]) + m["op"] + str(monkeys[m["nr"]]["val"])
			m["val"] = int(eval(os))

print(monkeys["root"]["val"])
