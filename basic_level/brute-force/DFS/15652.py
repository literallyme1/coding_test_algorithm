#백준 15652번 
# URL : https://www.acmicpc.net/problem/15652
#PyPy3 Code

#비내림차순 = 조합
N, M = map(int, input().split())

def backtrack(start, sequence):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    for num in range(start, N + 1):
        backtrack(num, sequence + [num])

backtrack(1, [])