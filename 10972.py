
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

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
    print(' '.join(map(str, a)))

# 1. 뒤에서 오름차순 깨지는 위치(i-1) 찾기
# 2. i-1보다 큰 수 중 제일 작은 수(j)랑 스왑
# 3. i부터 끝까지 오름차순 정렬