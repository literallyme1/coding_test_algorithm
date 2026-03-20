#[State] 처음에 DFS 생각 -> gpt 가 조건부 문제라고 함. -> 생각해보니, 거쳐가는 게 있어서 bfs 도 괜찮을 듯 
#[Input]  maps (미로)
# 문자열 배열 -> 2차원 배열 

# S : 시작 지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽

#[Logic] 
# 통로 0 -> 갈 수 있음. 벽 x
# 레버를 지나서 가야함.  

# 1. start -> lever 
# 2. lever -> end 

#[Output] 한 칸 1초, 최소값, 탈출 불가능 -1 

from collections import deque

#[문제점]
#1. 직선거리로 품. (벽을 간과)

# 틀린 것 3 : 좌표는 r, c 로 통일 넣을 때도 이순서로 
# 왜 이건 bfs 인지도 파악 
def bfs(start, target, maps):
    queue = deque()
    col = len(maps[0])
    row = len(maps)
    visited = [[False] * col for _ in range(row)]
    dc = [0,0,1,-1]
    dr = [1,-1,0,0]

    (sr, sc) = next((r, c) for r in range(row) for c in range(col) if maps[r][c] == start) # 코드 해석 필요 

    queue.append((sr, sc, 0)) #1. 틀린 것 : dist 는 0 부터 시작 
    visited[sr][sc] = True
    while queue:
        nr, nc, dist = queue.popleft() 

        if maps[nr][nc] == target:
            return dist
        
        for i in range(4):
            c = nc + dc[i]
            r = nr + dr[i]
            if 0 <= c < col and 0 <= r < row:
                if maps[r][c] != "X" and not visited[r][c]: #틀린 것 2. L, S 등 모두 o 에 해당
                    queue.append((r, c, dist + 1)) 
                    visited[r][c] = True
    return -1
                

def solution(maps):
    maps = [[c for c in s] for s in maps] 
    # 1. start -> lever 
    dist1 = bfs("S", "L", maps)
    if dist1 == -1:
        return -1
    # 2. lever -> end 
    dist2 = bfs("L", "E", maps)
    if dist2 == -1:
        return -1
    return dist1 + dist2 # 틀린것4 : 못 갈 때도 파악 




print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))