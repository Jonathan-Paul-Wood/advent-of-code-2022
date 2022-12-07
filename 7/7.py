import re
from collections import defaultdict
from pathlib import Path

with open("input.txt") as f:
    s = f.read().strip()

instructions = s.split("\n")

currentDir = ''

path = Path("/")
totals = defaultdict(int)

# print(instructions)
for instruction in instructions:
    if re.search("\$ cd ", instruction):
        nextDir = instruction.split(' cd ')[1]
        path = path / nextDir
        path = path.resolve()
    if re.search("^[0-9]{1,} ", instruction):
        fileSize = int(instruction.split()[0])
        for p in [path, *path.parents]:
            totals[str(p)] += fileSize

answer = 0
for total in totals.values():
    if total <= 100000:
        answer += total
        
# print(totals)

# print(answer) # ANSWER: 1447046

#### part 2

answer2 = []
currentSize = list(totals.values())[0]
print(currentSize)
for total in totals.values():
    if currentSize - total <= 70000000 - 30000000:
        answer2.append(total)

print(min(answer2)) # ANSWER: 578710