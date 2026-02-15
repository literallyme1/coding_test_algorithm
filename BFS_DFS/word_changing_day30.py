
#[State] BFS 
#[Input] begin	target	words

from collections import deque
def str_check(now, word):
    diff = 0
    for (n, w) in zip(now, word):
        if n != w:
            diff += 1
    return diff == 1

def solution(begin, target, words):

    #1. target 단어가 있는 지 확인 
    if target not in words:
        return 0 
    
    #2. visited_list = set(depth, begin)
    queue = deque([(0, begin)])
    visited= set(begin)

    while queue:
        depth, now = queue.pop()
        next_depth = depth + 1
        for word in words:
            if word not in visited and str_check(now, word):
                if word == target:
                    return next_depth
                queue.append((next_depth, word))
                visited.add(word)

    return 0

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
#[Logic]

#while visited_list:
# zip 다른게 하나 true  (함수)
# true 일 시 넣기 
# if target 이 나오면 종료 total
#[Output]

#1. 한 선택지가 sort 요소에 있는대로 만 갈 수 있는 거 카운트  x -> 어차피 반복 
#2. 각각 depth 가 다른 걸 걱정? => 리스트가 하나 각각 분리가 필요 