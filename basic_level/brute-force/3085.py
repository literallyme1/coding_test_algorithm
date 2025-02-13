#백준3085번 
# URL : https://www.acmicpc.net/problem/3085
#PyPy3 Code

#(의사코드 3) 최대 연속된 사탕 개수를 구하는 메소드
def max_candy_count(board, N) :
    max_count = 1

    for i in range(N):
        row_count = 1
        col_count = 1 
        #가로 연속 개수 확인 
        for j in range(1, N): # 0 < j < N
            if board[i][j] == board[i][j - 1]: # 이전꺼랑 같은 게 아니면 개수 세기
                row_count += 1 
            else : 
                max_count = max(max_count, row_count)
                row_count = 1 #초기화 

            #세로 연속 개수 확인
            if board[j][i] == board[j - 1][i]:
                col_count += 1
            else:
                max_count = max(max_count, col_count)
                col_count = 1#초기화 
        
        # for문 종료 후 가장 큰 것 
        max_count = max(max_count, row_count, col_count)

    return max_count

# (의사코드 4)모든 사탕을 교환하는 완전탐색
def solve_candy_game(N, board):
    max_candies = 0

    for i in range(N):
        for j in range(N):
            #오른쪽  사탕이 있다면
            if j + 1 < N:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                max_candies = max(max_candies, max_candy_count(board, N))
                #원상복귀
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j] 

            #아래 사탕이 있다면 
            if i + 1 < N:
                # 교환
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                max_candies = max(max_candies, max_candy_count(board, N)) 
                # 원래대로 복구 
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j] 
    return max_candies

#(의사코드1)입력 
N = int(input().strip())

#리스트는 알파벳 단위로 저장 됨. 
board = [list(input().strip()) for _ in range(N)]

#(의사코드5)출력
print(solve_candy_game(N, board))