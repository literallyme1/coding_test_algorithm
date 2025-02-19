#DFS + BackTracking + 순열

#백준 15649번 
# URL : https://www.acmicpc.net/problem/15649
#PyPy3 Code

#sequence : 지금까지 선택한 숫자들
#visited : 이미 사용한 숫자 체크 

def backtrack(n, m, sequence, visted):
    # sequence 리스트에 m 개 있을 시 리턴
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return 
    
    #1부터 n까지 탐색 
    for i in range(1, n + 1):
        if not visted[i]: #아직 선택 X 다면 
            visted[i] = True
            sequence.append(i)
            backtrack(n, m, sequence, visted) # 이번 것 고정, 다음 자리 경우의 수 파악 
            sequence.pop()
            visted[i] = False


#입력 받기 
n, m = map(int, input().split())
visited = [False] * (n + 1)
backtrack(n, m, [], visited) #백트랙킹 시작 