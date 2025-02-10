#백준 1978번 
# URL : https://www.acmicpc.net/problem/1978
#PyPy3 Code

import sys
import math

def is_prime(n):
    #1은 소수가 아님. 
    if n < 2:
        return False
    #1외의 약수가 있는 지 판별 -> 수를 반으로 나눈 후, 나눠지는 지 확인 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#입력과 출력
n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
prime_count = sum(1 for num in numbers if is_prime(num))
print(prime_count)