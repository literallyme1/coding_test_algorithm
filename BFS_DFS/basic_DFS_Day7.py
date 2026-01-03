import sys 
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
node_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    node_list[a].append(b)
    node_list[b].append(a)

for nodes in node_list:
    nodes.sort()
visited_list = [ False for _ in range(N+1)]

def bfs(now):
    wait = deque()
    while True:
        visited_list[now] = True
        print(now, end=" ")
        for i in node_list[now]:
            if visited_list[i] == False:
                wait.append(i)
                print(visited_list[i])
        
        if len(wait) == 0:
            break
        now = wait.popleft()

bfs(V)

