#[State]

#[Input]n(row), m(column), board
#[Logic]
# while 문 
# #set 이름을 뭐라고 하지?
# same_set = set()
# for r in range(n):
#     for c in range(m):
#         if graph[r][c] ==  graph[r+1][c] ==  graph[r][c+1] ==  graph[r+1][c+1]:
#             same_set.update([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]) #set 도 묶는게 맞겠지? 

#중력 구현 
    #for c in range(m):
        #col_list = [graph[r][c] for r in range(r) if r != 0]
        # new_col_list = 남은 것 0 
        #다시 넣기 



#1. 찾고 
#2. 0 되고 
#4. 또 찾고 
#[Output] 블록이 지워질 지 출력 


# def solution(m, n, board):


graph = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
graph = [ [s for s in i] for i in graph] #1. 문자열 split 을 하려함. 2. 더 간단하게 하는 방법 존재할 듯 
print(graph)

#print(solution(4,	5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]))