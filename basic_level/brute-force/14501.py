import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    T = [] #상담 기간 
    P = [] #상담 수익 

    #입력값 받기 
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)

    #dp 테이블 생성성
    dp = [0] * (N + 1)

    for day in range(N):
        #날짜를 거쳐 번 돈 중 max 만 저장
        dp[day + 1] = max(dp[day + 1], dp[day]) #상담 안한 경우

        if day + T[day] <= N: #상담기간이 N을 넘지 않을때
            dp[day + T[day]] = max(dp[day + T[day]], dp[day] + P[day]) #이전에 벌 수 있는 돈과, 현재 돈 중 더 큰 거

    print(max(dp))

solve()