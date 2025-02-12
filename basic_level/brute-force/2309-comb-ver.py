import sys
from itertools import combinations 

heights = [int(sys.stdin.readline()) for _ in range(9)]

total_heights = sum(heights)

for exclude in combinations(heights, 2): #2가지 조합을 만들어줌.
    if total_heights - sum(exclude) == 100:
        result = sorted([h for h in heights if h not in exclude])
        for h in result:
            print(h)
        break