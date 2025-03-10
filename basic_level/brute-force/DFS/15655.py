#DFS + BackTracking + 조합 + 입력값

#백준 15655번 
# URL : https://www.acmicpc.net/problem/15655
#PyPy3 Code

N,M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = []

def backtrack(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return 
    
    # 첫번째 자리보다 작은 거 선택 X
    for i in range(start, N):
        result.append(numbers[i])
        backtrack(i + 1) #이전 숫자보다 다음 숫자가 커짐. 
        result.pop()

backtrack(0)
