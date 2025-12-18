
from collections import deque
import sys

sys.setrecursionlimit(10**6)

def init_graph(n, m):

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, N + 1):
        graph[i].sort()
    return graph

def dfs(current_node):
    visited_dfs[current_node] = True
    print(current_node, end=' ')

    for next_node in graph[current_node]:
        if not visited_dfs[next_node]:
            #쫄병이 끝날 때까지 종료 X
            dfs(next_node)


input = sys.stdin.readline
# 노드 수, 간선 수, 시작 노드 번호 
N, M, V = map(int, input().split())
visited_dfs = [False] * (N + 1) # 1부터 시작 

graph = init_graph(N, M)
dfs(V)


