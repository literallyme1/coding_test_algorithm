###day 2에 개수도 구하기 

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


def solution_length(m, n, puddles):
    # 1. DP 테이블을 매우 큰 수(INF)로 초기화 (최솟값을 구해야 하므로)
    INF = float('inf')
    dp = [[INF] * m for _ in range(n)]

    # 2. 웅덩이 마킹 (0-index 변환 주의)
    # puddles가 [c, r] 형태이므로 r-1, c-1로 접근
    for c, r in puddles:
        dp[r-1][c-1] = -1 

    # 3. 시작점 초기화 (거리는 0부터 시작)
    dp[0][0] = 0

    for r in range(n):
        for c in range(m):
            # 시작점이거나 웅덩이면 계산 건너뜀
            if (r == 0 and c == 0) or dp[r][c] == -1:
                continue
            
            # 왼쪽과 위쪽 값 가져오기 (인덱스 범위 체크 필수!)
            # 웅덩이(-1)이거나 범위 밖이면 INF로 취급해서 min에서 배제
            up = dp[r-1][c] if r > 0 and dp[r-1][c] != -1 else INF # -1 일 때만 확인하면 되니까 
            left = dp[r][c-1] if c > 0 and dp[r][c-1] != -1 else INF
            
            # 위와 왼쪽 중 작은 값에 +1
            min_dist = min(up, left)
            
            if min_dist != INF:
                dp[r][c] = min_dist + 1
    
    return dp[n-1][m-1]

print(solution_length(4, 3, [[2, 2]])) # 결과: 5 (0,0 -> 3,2 까지의 칸 수)


####2. 패딩 방식 가상의 테두리를 만들고 0으로 채움. 시작점을 1, 1로 
def solution(m, n, puddles):
    # 1. 도화지를 한 칸씩 더 크게 만듭니다 (n+1 x m+1)
    # 0번 행과 0번 열은 자동으로 0으로 채워진 '가짜 길'이 됩니다.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 2. 웅덩이 표시 (문제 좌표 그대로 사용 가능!)
    for c, r in puddles:
        dp[r][c] = -1

    # 3. 시작점 설정
    dp[1][1] = 1

    # 4. 루프는 진짜 길인 1부터 시작합니다.
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            # 시작점이거나 웅덩이면 건너뜁니다.
            if (r == 1 and c == 1) or dp[r][c] == -1:
                continue
            
            # [핵심] 위(r-1)와 왼쪽(c-1)을 그냥 더하면 끝!
            # 웅덩이(-1)가 있을 때만 0으로 취급해줍니다.
            up = dp[r-1][c] if dp[r-1][c] != -1 else 0
            left = dp[r][c-1] if dp[r][c-1] != -1 else 0
            
            dp[r][c] = (up + left) % 1_000_000_007

    return dp[n][m]

print(solution(4, 3, [[2, 2]])) # 결과: 4


###mod 는 매단계에서 해주는 게 좋음. (개수)