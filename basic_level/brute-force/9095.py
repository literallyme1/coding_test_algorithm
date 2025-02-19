#백준 9095번 
# URL : https://www.acmicpc.net/problem/9095
#PyPy3 Code

import sys

#최대 n이 10까지이므로 DP 테이블 크기 설정
dp = [0] * 11

#기본값 설정 
#dp[i], i 는 i 까지 1,2,3 으로 만들 수 있는 개수 
dp[1] = 1  # (1)
dp[2] = 2  # (1+1), (2)
dp[3] = 4  # (1+1+1), (1+2), (2+1), (3)

# ex) dp[4]를 만드는 방법(합의 원리) = dp[3] + dp[2] + dp [1] 
# 마지막 수가 각각 1, 2, 3일 때를 가정, 이 수를 하나씩 고정했을 때 경우의 수수
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n])