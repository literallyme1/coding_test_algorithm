#[state] dfs
#[input] n, computers
#[logic] 무리 
#[output] 네트워크의 개수



n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
count = 0 

visited = [False] * n

def dfs(i):
    visited[i] = True

    for j in range(n):
        if computers[i][j] and not visited[j]:
            dfs(j)


for i in range(n):
    if not visited:
        dfs(i)
        count += 1



















visited = [False] * n 
def dfs(current):
    
    visited[current] = True

    for i in range(n):
        if not visited[i] and computers[current][i]:
            dfs(i) 

for i in range(n):
    if not visited[i]:
        dfs(i)
