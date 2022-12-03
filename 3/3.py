file = open('input.txt')

contents = file.readlines()

# rucksackCount = len(contents)

itemPriorityDict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

# print('a' > 'b')
# print('a' > 'A')
# print('a' > 'F')
# print('A' > 'B')
# print(contents[0])
# print(len(contents[0]))
# length = len(contents[0]) - 1
# print(length)
# print(int(length/2))
# print(contents[0][(int(length/2)):len(contents[0])])


def getPrioritySumOfMatches(sacks):
    totalSum = 0
    # for each sack
    # print(len(sacks))
    for sack in sacks:
        compartmentOne = sack[0:int(len(sack)/2)]
        compartmentTwo = sack[int(len(sack)/2):(len(sack) - 1)]
        # for each item
        for item in compartmentOne:
            # compare to items in other sack
            # when find match, use dict to sum numbers
            if (compartmentTwo.find(item) > -1):
                # print(item)
                # print('item:', item)
                # print('value to add: ', itemPriorityDict[item])
                totalSum += itemPriorityDict[item]
                # print('new total: ', totalSum)
                break
    
    print(totalSum)

# getPrioritySumOfMatches(contents)

def getBadges(sacks):
    totalSum = 0
    numGroups = int(len(sacks) / 3)
    i = 0
    while i < numGroups:
        bagOne = sacks[0 + i*3]
        bagTwo = sacks[1 + i*3]
        bagThree = sacks[2 + i*3]

        for item in bagOne:
            if ((bagTwo.find(item) > -1) and (bagThree.find(item) > -1)):
                print(item)
                print(itemPriorityDict[item])
                totalSum += itemPriorityDict[item]
                break
        
        i += 1
    print(totalSum)

getBadges(contents)