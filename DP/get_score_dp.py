
def solution(land):

    n = len(land)
    #1. DP 테이블 
    dp = [ [0] *  4 for _ in range(n) ]

    dp[0] = land[0][:]

    #2. 두번 째 줄부터 계산
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k != j) 

    return max(dp[n-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])