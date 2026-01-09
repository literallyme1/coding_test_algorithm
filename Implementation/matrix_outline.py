#[State]
#[Input] 행렬의 세로 길이(행 개수) rows 2 이상 100, 가로 길이(열 개수) columns2 이상 100, 
# 그리고 회전들의 목록 queries  1 이상 10,000 이하
#[Logic]
#시계방향 회전 -> 회전은 (x1, y1, x2, y2)인 정수 4개로 표현 -> x2- x1 + 1 : 세로, y2 - y1 + 1 : 가로 
# 각 쿼리 후 바뀐 수 가장 작은거 -> 배열 넣기 
#  내부는 회전 X

#1. 그래프 만들기 (만들어야 다음을 기억)
# graph = [ [j] for j in range(1, rows + 1) for i in range(1, columns+ 1)] #이중이면 뭐가 먼저인지 햇갈

#2. window 로 가져옴. 
    #window_index = [(x,y)  2중 포문 if not include 리스트 안 값]

    # 가져오기

#3. 돌리기 -> list 마지막을 첫번째로 append 
#4. 다시 넣기 
#5. 최솟값 넣기 
#[Output] 








# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.



