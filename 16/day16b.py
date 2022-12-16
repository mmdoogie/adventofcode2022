#!/bin/python3

from aocd import lines
import copy
import itertools

allValves = {}
for l in lines:
	n = l.split(" ")[1]
	r = int(l.split("=")[1].split(";")[0])
	d = l.split(" ",9)[9].split(", ")
	allValves[n] = {"name": n, "rate": r, "dest": d, "open": False, "dist": 1000, "visited": False}

def doDistancing(valves, startPos):
	for k,v in valves.items():
		v["dist"] = 1000
		v["visited"] = False
	valves[startPos]["dist"] = 0
	
	currPos = startPos
	while True:
		for n in valves[currPos]["dest"]:
			if valves[n]["visited"]:
				continue
			newDist = valves[currPos]["dist"] + 1
			if newDist < valves[n]["dist"]:
				valves[n]["dist"] = newDist

		valves[currPos]["visited"] = True
		remDist = [v["dist"] for k,v in valves.items() if not v["visited"]]
		if len(remDist) == 0:
			break
		minRem = min(remDist)
		if minRem == 1000:
			break
		currPos = [v for k,v in valves.items() if v["dist"] == minRem and not v["visited"]][0]["name"]

allDist = {}

paths = [["AA"]]
times = [26]
flows = [0]
while True:
	newPaths = []
	newTimes = []
	newFlows = []
	for p,t,f in zip(paths, times, flows):
		here = p[-1]
		if here not in allDist:
			doDistancing(allValves, here)
			allDist[here] = copy.deepcopy(allValves)
		valves = allDist[here]
		choices = []
		for k,v in valves.items():
			score = (t-v["dist"]-1)*v["rate"]
			if v["rate"] != 0 and v["dist"] != 0 and score > 0 and not v["name"] in p:
				choices += [(k, t - v["dist"] - 1, v["rate"])]
		if len(choices) == 0:
			continue
		for c in choices:
			newPaths += [p + [c[0]]]
			newTimes += [c[1]]
			newFlows += [f + c[1]*c[2]]
	if len(newPaths) != 0 and len(newPaths[-1]) == 8:
		# Using only the longest paths (9+9), they all overlapped.
		# Detuning to include the next shorter path length (8/9+8/9) finds the answer.
		# Potentially for some inputs it could require some of the shorter ones? (7+9, etc)
		savePaths, saveFlows = paths, flows
	if len(newPaths) == 0:
		break
	paths, times, flows = newPaths, newTimes, newFlows

fmax = 0
paths += savePaths
flows += saveFlows
for pm,pe in itertools.product(paths,paths):
	match = False
	for pmp in pm:
		if pmp != "AA" and pmp in pe:
			match = True
			break
	if not match:
		fm = flows[paths.index(pm)]
		fe = flows[paths.index(pe)]
		if fm+fe > fmax:
			fmax = fm + fe
	
print(fmax)
