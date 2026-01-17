#[State] 리스트 
#[Input] rows	columns	queries
#[Logic] 
#graph 만들기 ((i-1) x columns + j)
#[(row * columns) + [(j + 1) for j in range(colums) ]for row in range(rows)]
#행렬 -> 직사각형 파악 (인덱스 , 값) -> 시계방향 회전 
#인덱스 일일히 구해야 함 -> 순서 존재
# for query in queries : 
#인덱스 보정 조심 
    #for 문 4번 , 값과, 인덱스 저장 
    #deque.rotate(), 인덱스 for문 -> 값넣기 
    #min_list 에 값 중 가장 작은 거 넣기 
#가장 작은 거 min_list
#[Output] -> 순서대로는 그냥 반환 해야 함. 
