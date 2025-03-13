import sys
import math
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = math.inf
visited = [False] * n

#배치 완료시 계산
def calc():
    start_team = 0
    link_team = 0

    for i in range(n) :
        for j in range(n):
            if visited[i] and visited[j]:
                start_team += s[i][j]
            elif not visited[i] and not visited[j]:
                link_team += s[i][j]
    return abs(start_team - link_team)

#팀 배치 
def solve(depth, start):
    global min_diff

    if depth == n // 2:
        diff = calc()
        min_diff = min(min_diff, diff)
        return
    # 1을 기준으로 경우의 수, 1,2 경우의 수 이렇게 백트래킹
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False
    

solve(0, 0)
print(min_diff)