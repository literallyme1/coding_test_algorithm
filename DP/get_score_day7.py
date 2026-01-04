# [State]
# - dp -> land 사용 
# - 초기값: dp[0] 리스트 그대로 가져감. 

# [Input]
# - 데이터 리스트 입력받기

def solution(land):
    N = len(land)
    for row in range(1, N):
        for col in range(4):
            land[row][col] =  max(land[row-1][j] for j in range(4) if col != j) + land[row][col]# 이거 자체가 리스트야? 함수는 내부의 제너레이터가 생성한 값들 중에서 가장 큰 '값(정수)' 하나 반환 
    return max(land[-1])

# [Logic] 핵심 점화식 적기 (여기에 10분 투자)
# - 점화식: dp[i] = max(dp [i X] ) + i  | dp[row][i] = land[row][i] + max(dp[row-1][:i] + dp[row-1][i+1:])  | max_prev = max(land[row-1][j] for j in range(4) if j != i)
# - for list in land :, df_list = before_list, max(df_list.remove(i)) + list[i]

#2. for 문 
# for row in range(1, N): (두 번째 행부터 시작)
#   for i in range(4): (현재 행에서 내가 선택할 열)
#     # 이전 행(row-1)에서 현재 열(i)과 다른 열(j)들 중 최댓값 찾기
#     max_prev = max(land[row-1][j] for j in range(4) if j != i)
#     land[row][i] += max_prev (현재 위치에 최댓값 누적)

# [Output]
# - max(land[-1])

land  = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))