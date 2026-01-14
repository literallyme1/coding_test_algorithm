#[State] 주어진 2차원 배열 그대로 
#[Input] land (n <100,000)
#[Logic] graph[n][4] 
# dp[0] -> 그대로 
#for row in range(n):
    #dp[row][0] = max([dp[이전][j] for j in range(4) if i != 0]) + dp[row][0](기존 현재값)
    #dp[row][1] = max(dp[이전][j] for j in range(4) if i != 1)+ dp[row][0](기존 현재값)
    #dp[row][2] = max(dp[이전][j] for j in range(4) if i != 2)+ dp[row][0](기존 현재값)
    #dp[row][3] = max(dp[이전][j] for j in range(4) if i != 3)+ dp[row][0](기존 현재값)

#같은 열을 연속 X
#[Output] return 점수의 최대값 max(dp[-1]) 
