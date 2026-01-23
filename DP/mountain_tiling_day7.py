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


def solution(n, tops):
    dis_num = 10007
    intrude, not_intrude = 0, 1
    for i in range(n):
        prev_not, prev_in = not_intrude, intrude
        if tops[i] == 1: 
            not_intrude = (3 * prev_not + 2 * prev_in) % dis_num 
            intrude = (prev_not + prev_in) % dis_num
        else :
            not_intrude = (2 * prev_not + prev_in) % dis_num
            intrude = (prev_not + prev_in) % dis_num
    
    return (not_intrude + intrude) % dis_num



print(solution(4,[1, 1, 0, 1]))