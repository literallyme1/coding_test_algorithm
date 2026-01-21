
#Input] begin	target	words

#Logic begin -> target
#target 이 있나확인 

#[State]
#queue = deque(lamda[0,0])
#visited_list = set()

#1. target 이 있나확인 
# begin, 0 큐, visited_list
#while queue >0 :

#leftpop -> for i in ragnge(3) -> diff 하나인지  
    #하나면 기존 팝한 거 index2에 +=1 해서 넣기
#하나의 알파벳 
#Output 단계 return 


####현재 함수(각 인덱스) 

from collections import deque

def checking_word(now, new_node):
    diff = 0
    for (a, b) in zip(now, new_node):
        if a != b:
            diff += 1
    return diff <= 1

def solution(begin, target, words):
    queue = deque([(begin,0)])
    words.remove(begin)

    if target not in words:
        return 
    
    while queue :
        now, level = queue.popleft()
        if now == target: return level
        #new_words = [word for word in words if word not in visited_list]
        
        for new_word in words:
            if checking_word(now, new_word):
                queue.append([(new_word, level + 1)])
                words.remove(new_word)
    return 0 

        

