#중복순열 + 값지정 

#백준 15656번 
# URL : https://www.acmicpc.net/problem/15656
#PyPy3 Code

def backtracking(result):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(N):
        result.append(nums[i])
        backtracking(result)
        result.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

backtracking([])
