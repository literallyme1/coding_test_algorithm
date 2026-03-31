#[State] recursion 
#[Input] numbers , target
#[Logic] 
# 재귀 
#[Output] 방법의 수 count 

import sys
sys.setrecursionlimit(10**6)

def dfs(i, bool, numbers):
    if i == n - 1:
        return  numbers[i]
    
    dfs(i + 1,True, numbers)
    dfs(i + 1,False, numbers)
    

    

def solution(numbers, target):
    count = 0
    n = len(numbers)
    
    dfs(num, 0)
    dfs(-num, 0)
    return count 