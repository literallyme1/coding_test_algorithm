
def solution(m, n, board):
    #m : 판의 높이, n : 길이
    board = [list(row) for row in board]
    total_count = 0
    while True:
        # Scanning
        pop_list = []
        for col in range(m - 1):
            for row in range(n - 1):
                window_list = [board[col][row], board[col + 1][row], board[col][row + 1], board[col + 1][row + 1]]
                #만약 4개가 같다면 
                #if set(window_list) != 0 and len(set(window_list)) == 1:
                # if len(set(window_list)) == 1 and (0 for i in list(set(window_list))):
                if len(set(window_list)) == 1 and board[col][row] != 0:
                    pop_list.extend([(col,row), (col + 1,row), (col,row + 1), (col + 1,row + 1)])
        
        #while 문 종료 조건
        if(len(pop_list) == 0): break

        #Count Updated
        total_count += len(set(pop_list))
        #0으로 변환 
        for col, row in  list(set(pop_list)):
            board[col][row] = 0

        #중력구현 (col 과 row 를 다르게 씀. )
        #컬럼 가져오기 
        for row in range(n):
            colum = []
            for col in range(m):
                if board[col][row] != 0: colum.append(board[col][row]) 
            column = [0] * (m - len(colum)) + colum
            for index in range(m):
                board[index][row] = column[index]
                
    return total_count


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))