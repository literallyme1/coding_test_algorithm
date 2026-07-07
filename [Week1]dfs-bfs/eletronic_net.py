#[state]
#[Input] 송전탑의 개수 n, 그리고 전선 정보 wires
#[Logic]
# 전선 끊어 2개, 송전탑 비슷. 
#하나씩 끊어서. 가장 큰거. 

#[Output] 송전탑 개수의 차이(절대값)

def solution(n, wires):
    answer = n

    # 인접 리스트 만들기
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, blocked_a, blocked_b, visited):
        #  1. 현재 노드 방문 처리
        visited[node] = True
        # 현재 네트워크의 송전탑 개수
        count = 1

        # 연결된 송전탑 탐색
        for next_node in graph[node]:

            # 2. 현재 끊은 간선이면 건너뛰기
            if (node == blocked_a and next_node == blocked_b
                )  or (node == blocked_b and next_node == blocked_a) :
                continue

            # 3. 미방문 노드라면 DFS 결과 누적
            if not visited[next_node]:
                count += dfs(next_node, blocked_a, blocked_b, visited)

        # TODO 4. 연결된 송전탑 개수 반환
        return count

    # 간선을 하나씩 끊어보기
    for a, b in wires:
        visited = [False] * (n + 1)

        # TODO 5. 간선 (a, b)를 끊은 상태에서 한쪽 노드 수 구하기
        count = dfs(1, a, b, visited)

        # TODO 6. 두 전력망의 송전탑 개수 차이 계산
        difference = abs(count - (n - count))

        # TODO 7. 최솟값 갱신
        answer = min(difference, answer)

    return answer