#[state] bfs
#[input] maps, 0 은 벽, 1은 길 
#[logic] 나 (1,1) 상대(n, m)
#bfs 업데이트, visited , while 
#[output] 최단거리 return, 없을 시 -1 

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 도착점 확인
        if n - 1 == x and m - 1 == y:
             return dist
        
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인
            if 0 <= nx < n and 0 <= ny < m :
                    
                # 길이고 미방문인지 확인
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    # 방문 처리
                    visited[nx][ny] = True
                    # 거리 + 1로 큐에 삽입
                    queue.append((nx, ny, dist + 1))

    return -1