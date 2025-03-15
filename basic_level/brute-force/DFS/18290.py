#백트래킹(DFS) + 중복조합 + 입력값
#백준 18290번 
# URL : https://www.acmicpc.net/problem/18290
#PyPy3 Code

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#상하좌우  방향 정의 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#방문 체크
visited = [[False] * M for _ in range(N)]

max_sum = float('-inf') #음의 무한대 

def is_valid(r, c):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        #범위 해당하는 것중에 선택한 게 있으면 
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]:
            return False
    return True

def backtrack(count, total, start_r, start_c):
    global max_sum #함수 밖에서 정의된 변수 수정을 위해 사용 
    if count == K:
        max_sum = max(max_sum, total)
        return
    for r in range(start_r, N):
        for c in range(start_c if r == start_r else 0, M):  #하고 있는게 있으면 거기부터, 아니면 처음부터 
            if not visited[r][c] and is_valid(r, c):
                visited[r][c] = True
                backtrack(count + 1, total + board[r][c], r, c)
                visited[r][c] = False

backtrack(0, 0, 0, 0)
print(max_sum)