#백준 6064번 
# URL : https://www.acmicpc.net/problem/6064
#PyPy3 Code

import sys
import math

def find_k(M, N, x, y):
    #최소공배수 계산
    LCM = (M*N) // math.gcd(M, N)

    #최소공배수가 넘어가면 주기가 반복됨. 
    while x <= LCM:
        if (x-1) % N + 1 == y: #x가 현재년도라고 가정 
            return x
        
        x += M # M 이 될 때 x는 같은 수가 되므로 
    return -1

T = int(sys.stdin.readline().strip())
results = []

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    results.append(find_k(M, N, x, y))

#출력
sys.stdout.write("\n".join(map(str, results)) + "\n")