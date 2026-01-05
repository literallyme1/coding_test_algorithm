#[State] 2차원 배열 그대로 사용
#[Input]  board[m][n] 2 ≦ n, m ≦ 30 
#[Logic]  2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻음
# 여러 2×2에 포함될 수 있기에 다 찾고 한 번에 지워야 함. 
#1. 탐색
# window = [(x,y),(x,y+1),(x+1,y),(x+1,y+1)]
#for i in range(m-1):
    #for j in range(n-1):
        #if board[i][j] and ... 
            #set에 넣기 
#2. 지우기
#set 해당 ->  ex_block_count
#for i in set -> 0

#3. 중력 구현  
# for j in range(n-1):
    #list a = [board[i][j] for i in range(m-1) if i != 0]
    # list a = [0] * n - len(a) + a
    #넣어주기 
    #for 문 
# 
# -> 반복 while 문 과 조건 
# ex_block_count = 0 
#[Output] return ex_block_count
