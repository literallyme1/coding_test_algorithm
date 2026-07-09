#[state]
#[input] n, 어피치가 맞힌 과녁 점수의 개수 10 - 0 배열 info
#[logic] 
#[같은 과녁] 같은 발 -> 어피치, 다른 발 -> 많이 쏜 사람 이 그 과녁 가져감.
# 둘 다 0이면 아무도 안가져감. 
# 최종 점수가 동일 -> 어피치 승리
#무조건 지거나 비기는 경우 [-1]

#하나만 화살이 높거나, 0이거나. true or false. 
# DFS, 현재 점수 , DFS 선택, DFS 선택 x 
#[output]과녁 점수 10점부터 0점까지 순서대로 정수 배열, 가장 낮은 점수를 더 많이 맞힌 경우 return 

def solution(n, info):
    lion = [0] * 11
    answer = [-1]
    max_diff = 0

    def is_better(candidate, current):
        # 낮은 점수부터 화살 수 비교
        for i in range(10, -1, -1):
            if candidate[i] != current[i]:
                return candidate[i] > current[i]
        return False


    def dfs(idx, remain):
        nonlocal answer, max_diff

        # 종료 조건:
        # 11개 점수를 모두 확인한 경우
        if idx == 11:
            # 남은 화살을 0점에 넣기
            lion[10] += remain
            # 라이언 점수, 어피치 점수 계산

            lion_score = 0
            apeach_score = 0

            for i in range(11):


                if lion[i] == 0 and info[i] == 0:
                    continue
            # 점수 차이 비교 후 정답 갱신
                if info[i] < lion[i]:
                    lion_score += 10 - i
                else:
                    apeach_score += 10 - i

            diff = lion_score - apeach_score

            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = lion[:]
                elif diff == max_diff and is_better(lion, answer):
                    answer = lion[:]

            # 0점에 넣었던 화살 복구 -- 왜 remain 을 저렇게 하는건지 이해가 안됨. 
            lion[10] -= remain
            return

        need = info[idx] + 1

        # 현재 점수를 가져가는 경우
        if remain >= need:
            lion[idx] = need
            dfs(idx + 1, remain - need)

        # 현재 점수를 포기하는 경우
        dfs(idx + 1, remain)

    dfs(0, n)

    return answer