#[State]

#[Input]n(row), m(column), board

def solution(n, m, board):
#[Logic]
# while 문 


    total_count = 0 
    while True:
        remove_set = set()
        #1. 훑으면서 같은 블록 찾고 set 에 넣기 
        for r in range(n):
            for c in range(m):
                if r == n-1 or c == m - 1:
                    continue
                if graph[r][c] ==  graph[r+1][c] ==  graph[r][c+1] ==  graph[r+1][c+1] and graph[r][c] != "":
                    remove_set.update([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])
        
        ## While Condition 조건
        if len(remove_set) == 0:
            break
        #2. count 세고, Pop 을 ""로 표현하기 
        total_count += len(remove_set)
        for r, c in remove_set:
            graph[r][c] = ""

        #3.중력 구현 
        for c in range(m):
            col_list = [graph[r][c] for r in range(n) if graph[r][c] != ""]
            new_col_list = [""] * (n - len(col_list)) + col_list
            #다시 넣기 
            for i in range(n):
                graph[i][c]= new_col_list[i]
    return total_count

graph = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
graph = [ list(i) for i in graph] #1. 문자열 split 을 하려함. 2. 더 간단하게 하는 방법 존재할 듯 
print(solution(4,	5,	graph))