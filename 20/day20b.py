#!/bin/python3

from aocd import lines

k = 811589153

order  = [(k*int(l), n) for n, l in enumerate(lines)]
result = [(k*int(l), n) for n, l in enumerate(lines)]
count  = len(order)

for t in range(10):
	for o in order:
		src = result.index(o)
		dst = (src + o[0]) % (count - 1)
		if dst == 0:
			dst = count-1
		elif dst == count-1:
			dst = 0
		result.pop(src)
		result.insert(dst, o)

result = [r[0] for r in result]

idx0 = result.index(0)
idx1k = (idx0 + 1000) % count
idx2k = (idx0 + 2000) % count
idx3k = (idx0 + 3000) % count
print(idx0, idx1k, idx2k, idx3k, sum([result[idx1k], result[idx2k], result[idx3k]]))

