def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    visited = [[False] * cols for _ in range(rows)]

    # 상, 하, 좌, 우
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def dfs(x, y):
        # 1. 현재 칸 방문 처리
        visited[x][y] = True
        # 2. 현재 칸 식량으로 합계 초기화
        total = int(maps[x][y])

        # 3. 상하좌우 탐색
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 4. 범위 확인
            if 0 <= nx < rows and 0 <= ny < cols:
                 # 5. 바다가 아니고 미방문인지 확인 6. 재귀 결과 누적
                 if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    total += dfs(nx, ny)


        # TODO 7. 섬의 식량 합 반환
        return total 

    answer = []

    # 모든 칸 확인
    for x in range(rows):
        for y in range(cols):

            # TODO 8. 미방문 땅이면 DFS 시작
            if maps[x][y] != 'X' and not visited[x][y]:
                answer.append(dfs(x, y))

    # TODO 9. 섬이 없으면 [-1]
    if len(answer) == 0:
        print('-1') 

    # TODO 10. 오름차순 정렬 후 반환
    print(sorted(answer))   ## 오답 answer.sort() 반환 X 
