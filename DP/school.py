#[State]
#[Input] m(c), n, puddles(이차원 배열)
#[Logic] mod = 1,000,000,007

# 1. 2차원 배열 만들기 
# 2. arr[i][j] 기준 올 수 있는 경우 2가지 (왼, 위)
    # 왼 ,  위 max 
    # if 웅덩이 왼, 위에 있으면, 제외 
#[Output] 최단 경로 % 1,000,000,007

def solution(m, n, puddles):
    #1. 2차원 배열 
    dp = [[0 for _ in range(m)] for r in range (n)] 

    #2. puddle 마커
    for c, r in puddles:
        dp[r][c] = -1  ### 틀린것:  좌표는 1부터 시작하는 데 나는 0부터 시작 오류 

    #3. dp 식 재료 위 아래 
    for r in range(0, n):
        for c in range(0, m):
            # 웅덩이 일시 건너뛰기
            if dp[r-1][c] == -1 :
                dp[r][c] = dp[r][c-1] + 1
            elif dp[r][c-1] == -1:
                dp[r][c] = dp[r-1][c] + 1
            else :
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1
            dp[r][c]
    print(dp)
    return dp[n-1][m-1]


print(solution(4,3, [[2, 2]]))



## 인덱스 out of 범위 문제 해결법 
# 전제 : python 은 범위를 벗어나면 슬라이싱 처럼 -1, -2 보내줌.  <-> c, java 는안됨. 
#1. 경계 검사 inf 사용 






