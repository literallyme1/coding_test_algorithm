#[state]
#[input] places P(person), O(table), X(partition), 5*5
#[logic] 
# 좌표 미로찾기처럼 보면 됨. 
# 갈 수 있는 길, dist 사람 존재 -> 2 내라면 안적음,
# dist 2 일 시 둘 다 안지킴, 적고 둘 다 true -> 시작점은 어떻게 알지?
#[output] result (거리두기 yes 1 or no 0)


# 모든 P를 하나씩 시작점으로 잡고
# 각 P마다 visited를 새로 만들고
# X는 막힌 길로 처리하면서
# 거리 2까지만 BFS 탐색해.
# 그 안에서 다른 P를 만나면 해당 대기실은 0.

from collections import deque


def check_place(place):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    # 모든 칸을 확인
    for start_x in range(5):
        for start_y in range(5):

            # 1. P가 아니면 건너뛰기
            if place[start_x][start_y] == 'P':
                continue

            # 사람 한 명마다 visited 새로 생성
            visited = [[False] * 5 for _ in range(5)]

            # (x, y, 시작 사람으로부터 거리)
            queue = deque([(start_x, start_y, 0)])

            # 2. 시작 사람 방문 처리
            visited[start_x][start_y] = True
            while queue:
                x, y, dist = queue.popleft()

                # 3. 거리가 2이면 더 확장하지 않기
                if dist == 2:
                    continue

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    # 4. 범위 확인
                    if not (0 <= nx < 5 and 0 <= ny < 5):
                        continue
                    #  5. 방문한 칸이면 건너뛰기
                    if visited[nx][ny] and place[nx][ny] == "X":
                        continue
                    # 7. 다른 P를 발견하면 0 반환
                    if place[nx][ny] == 'P':
                        return 0

                    # TODO 8. 빈자리 방문 처리
                    visited[nx][ny] = True # 돌다가 다시 그자리 넣을 수 있음. 
                    # TODO 9. 큐에 좌표와 dist + 1 추가
                    queue.append((nx, ny, dist + 1))

    # TODO 10. 위반이 없으면 1 반환
    return 1


def solution(places):
    answer = []

    # TODO 11. 각 대기실을 검사해 결과 추가

    return answer