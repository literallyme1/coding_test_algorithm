#[State]
#[Input] money
#[Logic] 인접 x 최대값

#1. 처음 선택
#dp[i][0] = dp[i-1][x] + money[i]
#dp[i][x] = max(dp[i-1][o],  dp[i-1][x])
def solution(money):
    
    n = len(money)

    #1. 처음 선택
    o = money[0]
    x = money[0]
    for i in range(2, n - 1):
        temp_o = x + money[i]
        x = max(o, x)
        o = temp_o
    case_1 = max(o, x)

    o = 0
    x = 0
    for i in range(1, n):
        temp_o = x + money[i]
        x = max(o, x)
        o = temp_o
    case_2 = max(o, x)
    
    return max(case_1, case_2)
    #2. 처음 선택 x
#[Output] 최대값 

print(solution([1, 2, 3, 1]))