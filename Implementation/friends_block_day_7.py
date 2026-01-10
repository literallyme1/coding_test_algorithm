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

def solution(m, n, board): #m 이 row, 높이
    # 전처리 
    board = [ list(string) for string in board]
    total_count = 0
    
    while True:
        same_set = set()
        #1. 탐색 
        for i in range(m -1):
            for j in range(n -1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]: 
                    same_set.update([(i, j), (i + 1,j), (i,j + 1), (i + 1,j + 1)]) #튜플 넣는 사용법 틀림 
        
        #1-1 : 종료조건 
        if len(same_set) == 0:
            break

        #2. Same Count 
        total_count += len(same_set)

        #3. 0으로 지우기 
        for (i, j) in same_set:
            board[i][j] = 0

        #4. 중력구현 
        for col in range(n):
            col_list = [board[i][col] for i in range(m) if board[i][col] != 0]
            new_list = [0] * (m - len(col_list)) + col_list # 높이를 알려면 
            # [0 * (m - len(col_list))] + col_list
            for i in range(m-1):
                board[i][col] = new_list[i]
    return total_count
        
    
         
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))