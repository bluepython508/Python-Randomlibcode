import RandomEvents
from collections import Counter

results = []
for x in range(100):
    results.append(RandomEvents.roll())



results = [RandomEvents.roll() for x in range(100)]

c = Counter(results)

print (c)
print(results)
