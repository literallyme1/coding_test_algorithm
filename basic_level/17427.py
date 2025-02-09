#백준 17427번 
# URL : https://www.acmicpc.net/problem/17427
#python 3 Code

def calculate_g(N):
    g = 0
    # i가 약수로 등장하는 모든 경우를 계산
    for i in range(1, N + 1):
        g += i * (N // i)
    return g


N = int(input())
print(calculate_g(N))
