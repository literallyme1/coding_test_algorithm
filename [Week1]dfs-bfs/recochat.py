#[state] board
#[input]
#[logic]  "." : blank, "D" : block, "R" : robot, "G" : goal 
# R, G 는 . 으로 봄. 
# 미끄러짐을 어떻게 정의하는가 : 1. 가까운 block 찾기 2. 현재 x 나 y 가 같을 시 -> ( block + 1, -1 가까운데로 이동). 3. 없을 시 0반환 
#dist 넘기기, while 문 -> goal 좌표 일 시 중지 
#[output] 최소 이동 거리 

#1. 하나씩 살피는 게 아니라 쭉 미끄러짐. 
#2. 좌표 -> visited (여러군데 부딪힐 수 있으니.)


from collections import deque


def solution(board):
    rows = len(board)
    cols = len(board[0])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    start = None
    goal = None

    # 시작점과 목표점 찾기
    for x in range(rows):
        for y in range(cols):
            # 1. R이면 start 저장
            if board[x][y] == 'R':
                start = [x, y]
            # 2. G이면 goal 저장
            if board[x][y] == 'G':
                goal = [x, y]

    visited = [[False] * cols for _ in range(rows)]

    # (x, y, 이동 횟수)
    queue = deque([(start[0], start[1], 0)])

    # 3. 시작점 방문 처리
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        # 4. 현재 위치가 goal이면 dist 반환
        if goal[0] == x and goal[1] == y :
            return dist
        for dx, dy in directions:
            nx, ny = x, y

            # 한 방향으로 끝까지 미끄러짐
            while True:
                tx = nx + dx
                ty = ny + dy

                # 5. 다음 칸이 범위 밖이면 중단
                if not (0 <= tx < rows and 0 <= ty < cols):
                    break
                # 6. 다음 칸이 D면 중단
                if board[tx][ty] == "D":
                    break
                # 7. 이동 가능한 칸이면 nx, ny 갱신
                nx, ny = tx, ty 
            # 8. 제자리라면 건너뛰기
            if (nx, ny) == (x, y):
                continue


            # 9. 멈춘 위치가 미방문이면 방문 처리
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([(nx, ny, dist + 1)])


    # 11. 도달할 수 없으면 -1 반환
    return -1