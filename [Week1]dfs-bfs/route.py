#[state]
#[input] tickets  [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#[logic]
#ICN 출발  
# 한번에 넣고 시작하는게 나을까 vs for 문으로 돌아다니는 게 나을까..(전자가 낫다고 생각)
#1. 딕셔너리, 갈 수 있는 곳 넣고 정렬 
#2. dfs, 처음 나 배열넣기. 
#[output] 방문하는 공항 경로 배열


def solution(tickets):
    tickets.sort()

    used = [False] * len(tickets)
    route = ["ICN"]
    answer = []

    def dfs(current):
        # 종료 조건:
        # 모든 티켓을 사용했다면 정답 저장
        if len(route) == len(tickets) + 1: # icn 이 1을 담당 
            answer.extend(route)
            return True


        # 현재 공항에서 출발하는 티켓 탐색
        for i in range(len(tickets)):
            start, end = tickets[i]

            # 사용 가능한 티켓인지 확인
            if start == current and not used[i]:
                # 선택
                used[i] = True
                route.append(end)
                if dfs(end):
                    return True
                
                route.pop()
                used[i] = False

        return False

    dfs("ICN")

    return answer