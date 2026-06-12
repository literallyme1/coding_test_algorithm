#[state]
#[input] numbers
numbers =  "17"
#[logic]
#1. list 화 
numbers = [int(i) for i in numbers]

import math
#2. 소수 찾기
def is_prime(num):
    for i in range(1, math.sqrt(num)):
        if num % i == 0:
            return False
    return True

#3. dfs 함수 
visited = [False] * len(numbers)
def dfs(visited, curr, numbers, count):

    if is_prime(curr):
        count += 1
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            dfs(visited, i, curr * 10 + numbers[i], count)
            visited[i] = False
    return count
# 조건 1이 아니고, 2로 안나눠짐. 
# 조합 
#[output] 소수 개수 


