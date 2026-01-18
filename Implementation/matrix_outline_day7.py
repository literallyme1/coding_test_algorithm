#[State] 리스트 
#[Input] rows	columns	queries
#[Logic] 


#인덱스 일일히 구해야 함 -> 순서 존재
# for query in queries : 
#인덱스 보정 조심 
    #for 문 4번 , 값과, 인덱스 저장 
    #deque.rotate(), 인덱스 for문 -> 값넣기 
    #min_list 에 값 중 가장 작은 거 넣기 
#가장 작은 거 min_list
#[Output] -> 순서대로는 그냥 반환 해야 함. 

from collections import deque
def solution(rows, colums, querires):
    #graph 만들기 ((i-1) x columns + j)
    graph = [[(row * colums) + (j + 1) for j in range(colums)] for row in range(rows)]
    min_list = []
    #행렬 -> 직사각형 파악 (인덱스 , 값) -> 시계방향 회전 
    for query in querires:
        x1, y1, x2, y2 = [index -1 for index in query]
        value = []
        index_list = []

        #윗변 1
        for i in range(y1, y2):
            index_list.append((x1, i))
            value.append(graph[x1][i])
        #오른 변 2
        for i in range(x1, x2):
            index_list.append((i , y2))
            value.append(graph[i][y2])
            
        #아랫 변 3
        for i in range(y2, y1, - 1):
            index_list.append((x2, i))
            value.append(graph[x2][i])
        #왼 변 4
        for i in range(x2, x1, -1):
            index_list.append((i , y1))
            value.append(graph[i][y1])

        #deque.rotate(), 인덱스 for문 -> 값넣기 
        val_deq = deque(value)
        val_deq.rotate(1)

        for val_index, (i, j) in enumerate(index_list):
            graph[i][j] = val_deq[val_index]
        #min 수집
        min_list.append(min(value))
    
    return min_list
        


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))