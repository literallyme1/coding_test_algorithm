
from collections import deque
import sys


input = sys.stdin.readline
# 노드 수, 간선 수, 시작 노드 번호 
N, M, V = map(int, input().split())
visited_bfs = [False] * (N + 1) # 1부터 시작 
graph = [[] for _ in range(N + 1)]

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True # 방문 처리

    while queue:
        current_node = queue.popleft()
        print(current_node, end= ' ')

        for next_node in graph[current_node]:
            
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)