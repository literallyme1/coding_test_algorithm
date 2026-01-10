#[State]
#[Input] rows, columns, queries (1 ~ 10000)
#[Logic]
#시계방향 회전 -> 회전은 (x1, y1, x2, y2)인 정수 4개로 표현 -> x2- x1 + 1 : 세로, y2 - y1 + 1 : 가로 
# 각 쿼리 후 바뀐 수 가장 작은거 -> 배열 넣기 
#  내부는 회전 X

# graph = [ [j] for j in range(1, rows + 1) for i in range(1, columns+ 1)] #이중이면 뭐가 먼저인지 햇갈
def solution(rows, columns, queries):
    #1. 그래프 만들기
    graph = [[ (row * columns) + (j + 1) for j in range(columns)] for row in range(rows)]
    min_list = []
    
    #2. window 로 가져옴. (세부적 다시)
    for querie in queries:
        x1, y1, x2, y2 = querie
        square_list = []
        #윗가로
        for i in range(y1-1, y2-1):
            # square_list.graph[x1][i]
            # print(graph[x1][i])
            print(x1, i)
        #오른쪽 높이 
        for i in range(x1, x2 - 1):
            # square_list.graph[i][y2]
            # print(graph[i][y2])
            print(i, y2)
        #아랫가로
        for i in range(y2 - 2, y1 - 1, -1):
            # square_list.graph[x2][i]
            # print(graph[x2][i])
            print(x2, i)
        #왼쪽 높이 
        for i in range(x2-2, x1-2):
            # square_list.graph[i][y1]
            # print(graph[i][y1])
            print(i, y2)
        
    # #3. 회전 
    # last = square_list[-1].remove()
    # square_list.insert(0, last)

    # #4. 최솟값 리스트 
    # min_list.append(min(square_list))

    #다시 넣기 


    # 가져오기

#4. 다시 넣기 
#5. 최솟값 넣기 
#[Output] 





print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))


# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.



