#[State]
#[Input] maps 
#[Logic] 

# S : 시작 지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽
#[Output] 최소 시간 return, 탈출 안될 시 - 1

from collections import deque
def bfs(maps, start, goal):
    
    r = len(maps)
    c = len(maps[0])
    visited = [[False for _ in range(c)] for _ in range(r)]

    #start 위치 파악 
    (sr, sc) = next((r, c) for r in range(r) for c in range(c) if maps[r][c] == start) # 코드 해석 필요 

    #1. 레버까지 가는 최단경로 
    queue = deque()
    queue.append([0, sr, sc])

    ud = [0,0, 1, -1]
    rl = [1, -1, 0, 0]

    while queue:
        dist, nr, nc = queue.popleft()
        for i in range(4):
            nrr += ud[i]
            nc += rl[i]
            if 0 <= nr < r and 0 <= nc <c: 
                if maps[nr][nc] in ["O"] and not visited[nr][nc]:
                    queue.append([dist+1, nr, nc])
                elif maps[nr][nc] == goal:
                    return dist + 1
    return -1
        
                
def solution(maps):

    maps = [list(s) for s in maps]









    
maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
solution(maps)