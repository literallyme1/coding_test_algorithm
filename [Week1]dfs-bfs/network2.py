def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(node):
        #  1. 현재 컴퓨터 방문 처리
        visited[node] = True
        # 모든 컴퓨터 확인
        for next_node in range(n):
            # 2. 현재 컴퓨터와 연결되어 있고 미방문인지 확인
            if computers[node][next_node] == 1 and not visited[next_node]:
                # 3. 연결된 컴퓨터 DFS
                dfs(next_node)

    # 모든 컴퓨터 확인
    for node in range(n):

        # 4. 미방문 컴퓨터면 새로운 네트워크
        if not visited[node]:
            dfs(node)
            answer += 1
        

    return answer