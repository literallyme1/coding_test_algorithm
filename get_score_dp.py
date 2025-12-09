
def solution(land):

    #1. DP 배열 생성 
    input_len = len(land)
    dp1 = [0] * (input_len + 1)
    dp2 = [0] * (input_len + 1)
    dp3 = [0] * (input_len + 1)

    #2. 첫 값 
    dp1[1], dp2[1], dp3[1] = 1
    max_num = 0 
    
    #2. 같은 열 제외, 인덱스를 가는 3가지를 구하고 max 비교

    # 만약 첫 인덱스 가 1이면 제외 후 남은 인덱스 값을 넣음. 
    index_list = [0,1,2,3].remove(0)
    dp1[2] = land[0][index_list[0]]
    dp2[2] = land[0][index_list[0]]
    dp3[2] = land[0][index_list[0]]


    for i in range(2,input_len + 1):
        for 
        





    #3. max 파악 



solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
