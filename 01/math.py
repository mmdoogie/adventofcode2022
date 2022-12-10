import csv

with open("input2", mode = "r") as file:
	dat = csv.reader(file)
	textLines = [x for x in dat]

n = [[int(x) if x.isnumeric() else 0 for x in l] for l in textLines]

cal = [sum(x) for x in n]

print(n[0])
print(cal[0])
print(max(cal))

sc = cal.sort(reverse=True)
print(cal[0:3])
print(sum(cal[0:3]))
