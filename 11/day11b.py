#!/bin/python3

from aocd import lines

monkeys = []
for n in range(8):
	m = {}
	m["items"] = [int(x) for x in lines[n*7+1].split(":")[1].split(",")]
	ops = lines[n*7+2].split("= ")[1].split(" ")
	if ops[2] != "old":
		m["opv"] = int(ops[2])
		if ops[1] == "*":
			m["op"] = lambda x, y: x * y
		else:
			m["op"] = lambda x, y: x + y
	else:
		m["opv"] = 0
		m["op"] = lambda x, y: x * x
	m["tdiv"] = int(lines[n*7+3].split("by ")[1])
	m["dt"] = int(lines[n*7+4].split("monkey ")[1])
	m["df"] = int(lines[n*7+5].split("monkey ")[1])
	m["count"] = 0

	monkeys += [m]

mod = 1
for m in monkeys:
	mod *= m["tdiv"]

for n in range(10000):
	for m in monkeys:
		for i in m["items"]:
			m["count"] += 1
			worry = i
			worry = m["op"](worry, m["opv"])
			worry = worry % mod
			if worry % m["tdiv"] == 0:
				monkeys[m["dt"]]["items"] += [worry]
			else:
				monkeys[m["df"]]["items"] += [worry]
		m["items"] = []

cnts = [m["count"] for m in monkeys]
cnts.sort(reverse=True)
print(cnts[0] * cnts[1])
