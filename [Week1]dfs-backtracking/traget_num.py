#[state]
#[input] numbers(2개 이상 20개 이하)	target
#[logic]
# 1. 종료조건 cnt == len, target 이랑 같으면 경우의 수 + 1
# 2. return dfs(+arr[]), dfs(-arr[]) 
#[output] 경우의 수 



def dfs(result, i):
    if i + 1 == len(numbers):
        if result == target:
            ans += 1
            return
    return dfs(result + numbers[i], i + 1), dfs(result - numbers[i], i + 1)


    
    
numbers = [1, 1, 1, 1, 1]
target = 3

dfs(0, 0)











# dfs 는 언제 됐지 ?
#1. n 이 20 이하, -> 크다 bfs, 이전 -> 다음 영향 DP, 값이 무지막지하게 크다 Greedy
# 조정 
#1. index 만 넘기면 됨. 
#2. 함수 -> 전역, 넘길 거 제대로 파악 


