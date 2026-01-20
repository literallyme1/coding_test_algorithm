import sys
sys.setrecursionlimit(10**6)
### DFS

# [State] 재귀
# [Input] 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V,다음 M개의 줄에는 간선이 연결하는 두 정점의 번호
# - 리스트 N + 1, 각 리스트에 연결 노드 넣기(일방향), 정렬 
# [Logic] 처음 숫자, 인덱스에 들어가서 재귀 
# [Output] 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문


def dfs(now):

    visited_list[now] = True
    print(now)
    for i in node_list[now]:
        if visited_list[i]:
            continue
        dfs(node_list, visited_list) #부모 변수 쓸 수 있나?

# input = sys.stdin.readline()
N, M, V = map(int, input().split()) # 어떻게 하는 지 몰랐음.
node_list = [[] for _ in range (N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    node_list[a].append(b) # 일방향인 이유가 명확하지 X 
node_list.sort()

visited_list = [False for _ in range(N + 1)]



