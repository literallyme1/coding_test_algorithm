#[State] 
#[Input] 컴퓨터 개수 n, 연결 2차원 computers
#[Logic] # 네트워크, 직간접 포함. 

# visited_list(set), deque, 넣은 건 각각 0 [i][j], [j][i] = > 0 
# while queue : -> 하나 추가. 
# 
# #[Output] 네트워크의 개수

from collections import deque

def solution(n, computers):

    visited = [False] * n
    net_count = 0
    
    for i in range(n):
        if not visited[i]:
            net_count += 1
            queue = deque([i]) 
            visited[i] = True
            while queue:
                curr = queue.popleft()
                for neighbor in range(n):
                    if curr != neighbor and computers[curr][neighbor] == 1:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
    return net_count
print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
