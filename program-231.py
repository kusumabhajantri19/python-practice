
from functools import reduce
scores = [16,98,76,54,35,22]

# Increase all scores by 5 using map
updated = list(map(lambda x: x + 5, scores))

# Fillter only passing students (>=10)

passed = list(filter(lambda x: x >= 10, updated))

# Find only passing students using reduce

total = reduce(lambda x,y: x+y , passed)

print("updated:",updated)
print("passed:", passed)
print("total:", total)