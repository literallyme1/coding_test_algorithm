#[State]
#[Input] n(컴퓨터 개수), computers
#[Logic] 
#[Output]

from collections import deque

def solution(n, computers):
    visited = [False] * n
    queue = deque()
    count = 0 
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        queue.append(i)
        count += 1

        while queue:
            id = queue.popleft()
            for j, n in enumerate(computers[id]):
                if id != j and n == 1 and visited[j] == False:
                    visited[j] = True
                    queue.append(j)
    return count

print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


