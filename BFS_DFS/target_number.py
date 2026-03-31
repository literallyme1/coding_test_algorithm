#[State] recursion 
#[Input] numbers , target
#[Logic] 
# 재귀 
#[Output] 방법의 수 count 

import sys
sys.setrecursionlimit(10**6)

#재귀 사고
#1. 인자 (위에서 답, 아래서 답) -> 전해줘야 할 게 달라짐. 
#2. 탈출 조건 마지막에 원하는 값 (개수, 값, bool)
#3. 식 : 현재 위치에서 가능한 선택지 + 마지막에 가져온 요소를 어떻게 합할지 
    

    

def solution(numbers, target):
    n = len(numbers)
    def dfs(i, sum):
        if i == n:
            if numbers[i] == target:#배열 범위에 벗어나면
                return 1
            else:
                return 0
        return dfs(i + 1, sum + numbers[i]) +  dfs(i + 1, sum - numbers[i])
            
    count = 0
    n = len(numbers)
    
    dfs(num, 0)
    dfs(-num, 0)
    return count 