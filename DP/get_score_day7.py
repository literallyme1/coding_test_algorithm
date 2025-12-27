# [State]
# - dp -> land 사용 
# - 초기값: dp[0] 리스트 그대로 가져감. 

# [Input]
# - 데이터 리스트 입력받기

# [Logic] 핵심 점화식 적기 (여기에 10분 투자)
# - 점화식: dp[i] = max(dp [i X] ) + i 
# - for list in land :, df_list = before_list, max(df_list.remove(i)) + list[i]

# [Output]
# - max(land[-1])

### 틀린 것 
#1. remove 사용 X , = 는 얕은 복사 dp[row][i] = land[row][i] + max(dp[row-1][:i] + dp[row-1][i+1:])  | max_prev = max(land[row-1][j] for j in range(4) if j != i)
#2. for 문 
# for row in range(1, N): (두 번째 행부터 시작)
#   for i in range(4): (현재 행에서 내가 선택할 열)
#     # 이전 행(row-1)에서 현재 열(i)과 다른 열(j)들 중 최댓값 찾기
#     max_prev = max(land[row-1][j] for j in range(4) if j != i)
#     land[row][i] += max_prev (현재 위치에 최댓값 누적)