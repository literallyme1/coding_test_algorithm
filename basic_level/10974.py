
n = int(input())

visited = [False] * (n + 1)
path = []

def backtrack():
    if len(path) == n:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack()
            path.pop()
            visited[i] = False
backtrack()