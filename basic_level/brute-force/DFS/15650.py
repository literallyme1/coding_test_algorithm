#DFS + BackTracking + 조합

#백준 15650번 
# URL : https://www.acmicpc.net/problem/15650
#PyPy3 Code

def backtrack(n, m, start, sequence):
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return 
    
    # 첫번째 자리보다 작은 거 선택 X
    for i in range(start, n + 1):
        sequence.append(i)
        backtrack(n, m, i + 1, sequence) #이전 숫자보다 다음 숫자가 커짐. 
        sequence.pop()


#입력
n, m = map(int, input().split())
backtrack(n, m, 1, []) #1부터 시작 
