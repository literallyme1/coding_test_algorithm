
import sys
input = sys.stdin.readline

#1. 입력받기
n = int(input())
a = list(map(int, input().split()))

#2. 오름차순이 깨지는 지점 파악 
i = n - 1
while i > 0 and a[i - 1] <= a[i]:
    i -= 1

if i == 0:
    print(-1)

else: 
    j = n - 1
    #오름차순이 끊기는 왼쪽보다 오른쪽에서 큰 수 찾기 
    while a[i - 1] <= a[j]:
        j -= 1
    
    a[i - 1], a[j] = a[j], a[i - 1] #swap 

    a[i:] = reversed(a[i:]) 
    print(' '.join(map(str, a)))
