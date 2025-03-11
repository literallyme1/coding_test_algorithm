#백트래킹(DFS) + 중복조합 + 입력값
#백준 15657번 
# URL : https://www.acmicpc.net/problem/15657
#PyPy3 Code

N, M = map(int, input().split())
nums = list(map(int, input().split())).sort()

def backtrack(start, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N):
        backtrack(i, sequence + [nums[i]]) #중복 허용 

backtrack(0,[])