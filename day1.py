raw = """ """
# raw is a string containing the puzzle input

left = []
right = []

# parse string input
for line in raw.splitlines():
    line = line.split(" "*3) # Data is seperated by 3 spaces
    left.append(int(line[0]))
    right.append(int(line[1]))


# ok time for the actual advent

# Part 1
total_distance = 0

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    a = left[i]
    b = right[i]
    # total_distance += max(a, b) - min(a, b)
    big = max(a, b)
    small = min(a, b)

    # max-min ensures a positive distance
    total_distance += big - small


print(total_distance)

# Part 2
similarities = [] 
for i in left:
    multiplier = 0 # initial score multiplier
    for j in right: 
        if i == j:
            multiplier += 1
    similarities.append(i * multiplier)

print(sum(similarities))
