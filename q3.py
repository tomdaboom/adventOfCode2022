def priority(item):
    if 'a' <= item and item <= 'z':
        return ord(item) - 96
    elif 'A' <= item and item <= 'Z':
        return ord(item) - 38

rucksacks = []

with open("inputs/rucksacks.txt", "r") as f:
    for line in f:
        items = line[:-1]
        separator = int(len(items) / 2)
        rucksacks.append((items[0:separator], items[separator:]))

prioritySum = 0

for sack in rucksacks:
    for char in sack[0]:
        if char in sack[1]:
            prioritySum += priority(char)
            break

print("Part 1:", prioritySum)

badgeSum = 0

for i in range(0, len(rucksacks), 3):
    bag0 = rucksacks[i]
    bag1 = rucksacks[i+1]
    bag2 = rucksacks[i+2]

    for char in bag0[0]+bag0[1]:
        if char in bag1[0]+bag1[1] and char in bag2[0] + bag2[1]:
            badgeSum += priority(char)
            break

print("Part 2:", badgeSum)


