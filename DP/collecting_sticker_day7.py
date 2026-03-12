#[State]
#[Input] 
#[Logic] 스티커 1 -> 양옆 X
#1. 처음 사용 -> n - 1 까지 
# 첫 값 o = 10, x = 0 
# dp[i][o] = dp[i-1][x]
# dp[i][x] = max(dp[i-1][x], dp[i-1][o])
#[Output] 숫자 합의 최대값 

#2. 처음 사용 X n까지 
# 첫 값 o = 0, x = 1 


## 항상 경우의 수랑 햇갈림


def solution(sticker):
    n = len(sticker)
    #1. 첫 값 사용
    o = 10, x = 0 
    bef = True
    for i in range(2, n - 1):
        if bef == True:
            break
        else:
            