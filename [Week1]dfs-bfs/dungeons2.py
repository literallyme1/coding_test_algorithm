#[state] 백트래킹 dfs
#[input]
#[logic]
#[output]


def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0

    def dfs(fatigue, count):
        nonlocal answer

        # 1. 현재까지 방문한 던전 수로 최댓값 갱신
        answer = max(answer, count)  # -- 왜 이걸 여기서 하는 지 잘 모르겠음. 

        # 모든 던전을 다음 후보로 확인
        for i in range(len(dungeons)):
            required, cost = dungeons[i]

            # 2. 아직 방문하지 않았는지 확인 & 현재 피로도로 입장 가능한지 확인
            if not visited[i] and fatigue >= required:
                # 4. 현재 던전 방문 처리
                visited[i] = True
                # 5. 소모 피로도를 빼고, 방문 수를 1 증가시켜 재귀
                dfs(fatigue - cost, count + 1)
                # 6. 다른 순서를 탐색하기 위해 방문 취소
                visited[i] = False

    # 초기 피로도 k, 방문한 던전 수 0
    dfs(k, 0)

    return answer