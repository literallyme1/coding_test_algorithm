#[state] begin	target	words
#[input]
#[logic]
# 변환 X -> 0 반환
#[output] 최소 단계 

# 1. deque (단어, dist) 
# 2. visited 만들고, 파악 
# 3. while 문 안에서 처음 target 찾았는 지 확인

from collections import deque

def diff_count(curr, com):
    diff = 0

    # 4. 현재 단어와 후보 단어의 다른 글자 수 계산
    for a, b in zip(curr, com):
        if a != b:
            diff += 1 
        if diff > 1:
            return False
        return True
def solution(begin, target, words):
    # 1. target이 words에 없으면 0 반환
    if target not in words:
        return 0

    visited = [False] * len(words)

    # (현재 단어, 변환 횟수)
    queue = deque([(begin, 0)])

    while queue:
        current, dist = queue.popleft()

        # 2. target에 도착했으면 dist 반환
        if current == target:
            return dist

        # 모든 단어를 다음 후보로 확인
        for i in range(len(words)):
            # 3. 이미 방문한 단어면 건너뛰기
            if visited[i]:
                continue
            if diff_count(current, words[i]):
                # 5. 정확히 한 글자만 다르면 방문 처리
                visited[i] = True
                # 6. 큐에 다음 단어와 dist + 1 추가
                queue.append(words[i], dist + 1)


    # 7. 변환할 수 없으면 0 반환
    return 0
