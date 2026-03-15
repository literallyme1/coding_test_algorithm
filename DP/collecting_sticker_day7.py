#[State]
#[Input] 
#[Logic] 스티커 1 -> 양옆 X
#1. 처음 사용 -> n - 1 까지 
# 첫 값 o = 10, x = 0 
# dp[i][o] = dp[i][x] + sticker[i]
# dp[i][x] = max(dp[i-1][o], dp[i-1][x])

#2. 처음 사용 X n까지 
# 첫 값 o = 0, x = 1 

#[Output] 숫자 합의 최대값 
def solution(sticker):
    n = len(sticker)
    total = []
    #1. 첫 값을 사용한 경우 
    if n == 1:
        return sticker[0] ## 1. 첫값을 사용한 경우니까 x 도 sticker[0] 이 되어야 함. !!!
    o = sticker[0]
    x = sticker[0]
    for i in range(2, n - 1):
        temp_o = o
        temp_o = x +  sticker[i] # 2. 이전이 x 여야 o 가 가능 -> 점화식 오류 !!!
        x = max(o, x)
        o = temp_o
    total.append(o)
    #2. 첫 값을 사용하지 않은 경우
    o = 0
    x = 0
    for i in range(1, n):
        temp_o = o
        temp_o = x + sticker[i]
        x = max(o, x)
        o = temp_o
    total.append(o)

    return max(total)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))