#중복 순열

#1. 입력받기 
N, M = map(int, input().split())

#print 위한 리스트 
result = []

#백트래킹 함수 정의 
def dfs(depth):
    if depth == M:
        print(" ".join(map(str, result)))
        return 
    
    for i in range(1, N + 1):
        result.append(i)
        dfs(depth + 1)
        result.pop()

dfs(0)