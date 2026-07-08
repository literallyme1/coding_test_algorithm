#[state]
#[input]
#[logic]
#[output] 몇번째단어인지

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']

    order = 0
    answer = 0

    def dfs(current):
        nonlocal order, answer

        # 1. 빈 문자열이 아니면 현재 단어의 순번 증가
        if current:
            order += 1 

            # 2. 현재 단어가 목표 단어라면 정답 저장
            if current == word:
                answer = current
                # 찾았다는 의미로 True 반환
                return True

        # 3. 길이가 5라면 더 이상 문자 추가 불가
        if len(current) >= 5:
            return False

        # 4. A, E, I, O, U 순서대로 문자 추가
        for vowel in vowels:
            # 5. 자식 재귀에서 목표를 찾았다면 즉시 종료
            if dfs(current + vowel):
                break
        # 6. 목표를 찾지 못했다면 False 반환
        return False



    # 빈 문자열부터 탐색 시작
    dfs("")

    return answer