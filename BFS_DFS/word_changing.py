#[State] list
#[Input] begin	target	words
#[Logic]  begin -> target 으로 최소 변환 
#최단거리 
#1. 하나만 달라지는 거 찾음. 큐 
#2 queue 에 cog 가 있으면 중지. 없으면 반복 

# for word in words:
#word 별로 target 이 나오는 최단 경로 찾음 = bfs 
    # if  begin + word => len(set) == 1 => 큐 
        #count +=1 
    # if target in queue과 같으면 종료 -> 리스트에 넣어놓음. 

# return  max(최단거리 리스트)

#[Output] 최소 변환 count

#틀린점
#count 위치 -> 큐에 튜플 넣기 
# set 순서 고려 X -> zip 으로 비교 
#visitedlist 필요함. 
from collections import deque

def checking_word(now, target):
    diff = 0
    for i, j in zip(now, target):
        if i != j:
            diff += 1
    return diff == 1 

def solution(begin, target, words):

    visited_list = set()
    queue = deque()

    # WORDS 에 TARGET 이 없는 경우
    if target not in words:
        return 0
    
    #처음
    queue.append((begin, 0))
    visited_list.add(begin)


    while queue: 
        now, level = queue.popleft()
        not_visited_list = [word for word in words if word not in visited_list]
        #첫번째 
        for word in not_visited_list: 
            #같은 알파벳이 2개 챙김 
            if checking_word(now, word):
                if target == word:
                    return level + 1
                visited_list.add(word)
                queue.append((word, level + 1))



#bfs : now -> 갈수 있는 거 전부 
            




