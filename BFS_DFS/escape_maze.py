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

def range_cal(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
def solution(maps):
    maps = [[c for c in s] for s in maps] 
    col = len(maps[0])
    row = len(maps)
    queue = deque()
    visited = [[False for _ in range(col)] for _ in range(row)]
    # 1. start -> lever 
    x_w = [0,0,1,-1]
    y_w = [1,-1,0,0]
    # 최단 값 찾고 거리계산 생각 (따로 예상)
    min_range = 0 
    le_point = ()
    for r in range(row):
        for c in range(col):
            if maps[r][c] == "S":
                queue.append((r, c))
                visited[r][c] = True
                while queue:
                    y, x = queue.popleft() # r, c 하니까 변수 어떻게 쓸 지 x, y, x 햇갈림. 
                    for i in range(4):
                        t_x = x + x_w[i]
                        t_y = y + y_w[i]
                        if 0 <= t_x < col and 0 <= t_y < row:
                            if maps[t_y][t_x] == "O" and not visited[t_y][t_x]:
                                queue.append((t_y, t_x))
                                visited[t_y][t_x] = True
                            elif maps[t_y][t_x] == "L" and not visited[t_y][t_x]:
                                min_range += range_cal(c, r, t_y, t_x)
                                le_point = (t_y, t_x)
                                break 
    visited = [[False for _ in range(col)] for _ in range(row)]
    queue = deque()
    queue.append(le_point)
    #똑같이 찾음. 





    return 


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))