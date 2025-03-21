#백준 15654번 
# URL : https://www.acmicpc.net/problem/15654
#PyPy3 Code


#중복없는 순열, 입력값 0
#2,1 과 1,2 가 다르므로 start 대신 visted 사용 
N,M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = [False] * N
result = []

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if not visited[i]: #중복 방지
            visited[i] = True
            result.append(numbers[i])
            backtracking(depth + 1) #다음 단계
            result.pop()
            visited[i] = False
backtracking(0)