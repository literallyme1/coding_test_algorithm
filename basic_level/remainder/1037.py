#백준 1037번 
# URL : https://www.acmicpc.net/problem/1037

num_divisors = int(input())
divisors = list(map(int, input().split()))

divisors.sort()

#작은 약수와, 큰 약수의 곱 
N = divisors[0] * divisors[-1]

print(N)