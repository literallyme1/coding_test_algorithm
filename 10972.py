
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input()).split())

#2. 뒤에서 부터 오름차순이 끊기는 지점 파악
i = n - 1
while i > 0 and a[i - 1] >= a[i]:
    i -= 1

if i == 0:
    print(-1)
else:
    j = n - 1 
    while a[i - 1] > a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    a[i:] = reversed(a[i:])