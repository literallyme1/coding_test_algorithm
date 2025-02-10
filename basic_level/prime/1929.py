#백준 1929번 
# URL : https://www.acmicpc.net/problem/1929
#PyPy3 Code

import sys

#에라토스테네스의 체를 사용하여 범위 내 모든 소수를 찾는 함수수
def sieve_of_eratosthenes(limit):
    
    is_prime = [True] * (limit + 1) #처음 모든 수를 소수로 가정
    is_prime[0], is_prime[1] = False, False # 0, 1 은 소수가 아님.

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return is_prime

#입력과 출력 

M, N = map(int, sys.stdin.readline().split())
prime_list = sieve_of_eratosthenes(N)

for num in range(M, N+1):
    if prime_list[num]: #숫자 인덱스와 동일일
        print(num)