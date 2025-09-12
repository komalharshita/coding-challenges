import numpy as np
from collections import Counter

size = int(input())
array = list(map(int, input().split()[:size]))

mean = np.mean(array)
print(f"{mean:.1f}")

median = np.median(array)
print(f"{median:.1f}")

count = Counter(array)
maxc = max(count.values())
modes = []
for number, c in count.items():
    if c == maxc: 
        modes.append(number)

min_mode = min(modes)
print(min_mode)
