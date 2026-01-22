### top 0

#dp[이전][침범X] => dp[현재][침범X] : 3
#dp[이전][침범X] => dp[현재][침범0] : 1
#dp[이전][침범0] => dp[현재][침범X] : 2
#dp[이전][침범0] => dp[현재][침범0] : 1
# dp[현재][침범X] = 3* dp[이전][침범X] + 2 * dp[이전][침범0]
# dp[현재][침범0] =  dp[이전][침범X] + dp[현재][침범0] 

### top x

#dp[이전][침범X] => dp[현재][침범X] : 2
#dp[이전][침범X] => dp[현재][침범0] : 1
#dp[이전][침범0] => dp[현재][침범X] : 1
#dp[이전][침범0] => dp[현재][침범0] : 1

# dp[현재][침범X] = 2* dp[이전][침범X] + dp[이전][침범0]
# dp[현재][침범0] =  dp[이전][침범X] + dp[현재][침범0] 

#[State]
#[Input] n	tops
#[Logic]
#dp[0] = 침범 x : 1 침범 0 : 0 
# intrude  = 0
# not_intrude = 1

#for _ in range(n+1):
    #if 탑 있으면 
    #intrude
    #not intrude %
#[Output]