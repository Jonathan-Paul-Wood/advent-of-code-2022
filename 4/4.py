file = open('input.txt')

contents = file.readlines()

containsCount = 0
for pair in contents:
    elves = pair.split(',')
    elfOne = elves[0].split('-')
    elves[1] = elves[1].replace('\n', '')
    elfTwo = elves[1].split('-')

    if ((int(elfOne[0]) >= int(elfTwo[0])) and (int(elfOne[0]) <= int(elfTwo[1]))):
        containsCount += 1 # one all in two
    elif ((int(elfTwo[0]) >= int(elfOne[0])) and (int(elfTwo[0]) <= int(elfOne[1]))):
        print(elfOne, elfTwo)
        containsCount += 1



print(containsCount)