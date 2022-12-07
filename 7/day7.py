#!/bin/python3

from aocd import lines

files = []
currPath = []
for l in lines:
        p = l.strip().split(" ")
        if p[0] == "$":
                if p[1] == "cd":
                        if p[2] == "/":
                                continue
                        elif p[2] == "..":
                                currPath.pop()
                                continue
                        else:
                                currPath = currPath + [p[2]]
                elif p[1] == "ls":
                        continue
        else:
                if p[0] == "dir":
                        files += [{"path": "/".join(currPath + [p[1]]), "name": "_", "size": 0}]
                else:
                        files += [{"path": "/".join(currPath), "name": p[1], "size": int(p[0])}]

allPaths = set([x["path"] for x in files])

dirSizes = [{"path": p, "size":sum([f["size"] for f in files if f["path"].startswith(p)]) } for p in allPaths]

smallTotal = sum([s["size"] for s in dirSizes if s["size"] <= 100000])

print("Small dirs total: " + str(smallTotal))

usedTotal = sum([f["size"] for f in files])
freeSpace = 70000000 - usedTotal
neededSpace = 30000000
needToClear = neededSpace - freeSpace

deleteCandidates = [s for s in dirSizes if s["size"] >= needToClear]
deleteCandidates = sorted(deleteCandidates, key=lambda x: x["size"])

print("Smallest to clear space: " + str(deleteCandidates[0]["size"]))
