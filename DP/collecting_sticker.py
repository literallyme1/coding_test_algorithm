#[State] nlog(n) # BFS 는 너무 큰가? 
#[Input] sticker, 십만 이하, 각 칸에 적힌 숫자는 1 이상 100 이하
def solution(sticker):

    o, x = sticker[0], 0
    n = len(sticker)

    if n == 1:
        return sticker[0]
    #Case 1 : 첫번째 선택
    for i in range(1, n-1):
        temp_o = o
        o = x + sticker[i]
        x = max(temp_o, x)
    case1 = max(o, x)
    o, x  = 0, 0
    #Case 2 : 첫번째 선택 X
    for i in range(1, n):
        temp_o = o
        o = x + sticker[i]
        x = max(temp_o, x)
    case2 = max(o, x)
    
    
    return max(case1, case2)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
    
#[Logic] # 하나 선택, 양쪽 사용 불가 ,  숫자의 합이 최대 
#[Output]  스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값


#문제 이해 실패 -> 다시 또다른 원형이 되는 줄 앎. -> 입출력 예시를 먼저 꼭 보기 

# 값 
#첫번째 
# dp[i][0] = dp[i-1][x] + 현재값 
# dp[i][x] = max(dp[i-1][x], dp[i-1][0]) 

#첫번째 X
