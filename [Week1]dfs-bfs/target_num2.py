#[state] 백트래킹 x, dfs (순서가 정해져있으니까)
#[input] numbers, target
#[logic]
#[output] 타겟 넘버를 만드는 방법의 수 각각 dfs
# len 길이만 보내고 끝까지. 보고 결정. 


def solution(numbers, target):
    answer = 0

    def dfs(index, total):
        nonlocal answer

        # 1. 모든 숫자를 사용했는지 확인
        if index == len(numbers):
            # 2. 최종 합이 target이면 경우의 수 증가
            if total == target:
                answer += 1
            # 3. 더 이상 탐색하지 않고 반환
            return

        # 4. 현재 숫자를 더하는 경우 재귀
        dfs(index + 1, total + numbers[index]) # index + 1 인지 index 인지 햇갈림. 

        # 5. 현재 숫자를 빼는 경우 재귀
        dfs(index + 1, total - numbers[index]) # 현 인덱스를 쓰고 +1 로 나아간다. 

    # 0번 인덱스, 초기 합계 0부터 시작
    dfs(0, 0)

    return answer