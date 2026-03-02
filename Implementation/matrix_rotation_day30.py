#[State]

from collections import deque
#[Input] rows	columns	queries
def solution(rows, columns, queries):
    #1. Graph 만들기 
    graph = [ [(row * columns) + col for col in range(1, columns + 1)] for row in range(rows)]
    
    min_list = []

    #2. 회전 할 직사각형 파악 (for문 쿼리) 
    for query in queries:
        #인덱스, 값 리스트 
        index = []
        value = deque()  

        #첫, 끝 인덱스 파악 
        row1, col1, row2, col2 = [i-1 for i in query]
        width = col2 - col1 + 1
        height = row2 - row1 + 1
        # print(width, height)

        #1. 위 가로 
        for i in range(1, width):
            value.append(graph[row1][col1 + i])
            index.append((row1, col1 + i))
        #2. 우, 세로
        for i in range(1, height):
            value.append(graph[row1 + i][col2])
            index.append((row1 + i, col2))

        #3. 아래 가로 
        for i in range(1, width):
            value.append(graph[row2][col2 - i])
            index.append((row2, col2 - i))

        #2. 좌, 세로
        for i in range(1, height):
            value.append(graph[row2 - i][col1])
            index.append((row2 - i, col1))
        
        value.rotate()
        for ind, (row, col) in enumerate(index):
            graph[row][col] = value[ind]
        
        min_list.append(min(value))
    return min_list
            
            
print(solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#[Logic]


#retrun 할 리스트 

#x1, y1, x2, y2 = querie
#인덱스 리스트 
#rotate 할 리스트 (deque)
#3. deque.rotate()
#가장 작은 거 하나 넣기 
#4. 기존 인덱스리스트를 돌면서 넣기 
#[Output]
