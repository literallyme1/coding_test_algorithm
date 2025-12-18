
from collections import deque
import sys

def init_graph(n, m):

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, N + 1):
        graph[i].sort()
    return graph

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True # 방문 처리

    while queue:
        current_node = queue.popleft()
        print(current_node, end= ' ')

        for next_node in graph[current_node]:
            #방문 하지 않은 곳, 줄 세우기 
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)


input = sys.stdin.readline
# 노드 수, 간선 수, 시작 노드 번호 
N, M, V = map(int, input().split())
visited_bfs = [False] * (N + 1) # 1부터 시작 

graph = init_graph(N, M)
bfs(V)


