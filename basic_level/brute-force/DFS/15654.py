#중복없는 순열, 입력값 0
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