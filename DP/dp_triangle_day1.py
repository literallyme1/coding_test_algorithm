#[State] triangle 자체를 활용
#[Input] triangle
#[Logic] triangle[0] = 7 
#for r, row in enumerate (1, triangle):
    #len = len(row)
    #for c, value in enumerante row:
        #if c = 0 
        #triangle[r][c] = max( triangle[r-1][0] ) + 자신
        #elif 인덱스 가 마지막 
        ## triangle[r][c] = max( triangle[r-1][-1] ) + 자신
        #else:
        #triangle[r][c] = max(  triangle[r-1][c-1], tri[r-1][c] ) + 자신 


#dp[현재] = max(dp[이전, 현재 인덱스 - 1][오른쪽], dp[이전, 현재 인덱스][왼쪽], 자신 ) 
# 자기가 0 이거나, 자기가 가장 마지막이면 각각 오른쪽 왼쪽 X 

#[Output] 거쳐간 숫자의 최댓값을 return
