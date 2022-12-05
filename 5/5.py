import re

file = open('starting.txt')

starting = file.readlines()

crates = []

for row in starting:
    crates.append(re.findall(".{3}\s", str(row)))


rotated90 = list(zip(*crates[::-1]))
print(rotated90)
trimmedCrates = []
for arr in rotated90:
    trimmedCrates.append(re.findall("[A-Z]", str(arr)))
print(trimmedCrates)


file2 = open('input.txt')

moveSteps = file2.readlines()

### functions

def part1(data, movement):
    for move in movement:
        steps = re.findall("[0-9]{1,2}", move)
        amount = int(steps[0])
        pos1 = int(steps[1]) - 1
        pos2 = int(steps[2]) - 1

        moved = 0
        while moved < amount:
            data[pos2].append(data[pos1].pop())
            moved += 1
        
        print(data)
    
    print('answer: ')
    for d in data:
        print(d[len(d) - 1])


# part1(trimmedCrates, moveSteps)

def part2(data, movement):
    for move in movement:
        steps = re.findall("[0-9]{1,2}", move)
        amount = int(steps[0])
        pos1 = int(steps[1]) - 1
        pos2 = int(steps[2]) - 1

        print('move: ', (len(data[pos1]) - amount))
        data[pos2] = data[pos2] + (data[pos1][(len(data[pos1]) - amount):])
        data[pos1] = data[pos1][:(len(data[pos1]) - amount)]
        
        print(data)
    
    print('answer: ')
    for d in data:
        print(d[len(d) - 1])

part2(trimmedCrates, moveSteps)