
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

max_sum = 0

#모든 순열의 경우의 수를 비교함. 
for perm in permutations(a):
    total = 0
    for i in range(n - 1):
        total += abs(perm[i] - perm[i+1])
    max_sum = max(max_sum, total)
print(max_sum)