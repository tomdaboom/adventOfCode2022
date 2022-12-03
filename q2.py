calories = []

with open("inputs/calories.txt", "r") as f:
    curCals = []
    for line in f:
        if line != "\n":
            curCals.append(int(line))
        else:
            calories.append(curCals)
            curCals = []

totals = []

for cals in calories:
    sum = 0
    for c in cals:
        sum += c

    totals.append(sum)

totals.sort(reverse=True)
print(totals[0] + totals[1] + totals[2])


