#[State] 
#[Input] 컴퓨터 개수 n, 연결 2차원 computers
#[Logic] # 네트워크, 직간접 포함. 

# visited_list(set), deque, 넣은 건 각각 0 [i][j], [j][i] = > 0 
# while queue : -> 하나 추가. 
# 
# #[Output] 네트워크의 개수

from collections import deque

def solution(n, computers):

    queue = deque()
    net_count = 0

    #리스트 요소 vs range()
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                net_count += 1
                queue.append((i, j))
                computers[i][j] = 0 
                while queue:
                    a, b = queue.popleft()
                    computers[b][a] = 0
                    for c in range(n):
                        if b != c and computers[b][c] == 1:
                            queue.append((b, c))
                            computers[b][c] = 0 
    return net_count
 
print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
