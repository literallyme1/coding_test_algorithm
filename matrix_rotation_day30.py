#[State]
#[Input] rows	columns	queries
#[Logic]

#1. Graph 만들기 [ [(row * colums) + col for col in range(colums)] for row in range(rows)]
#retrun 할 리스트 
#2. 회전 할 직사각형 파악 (for문 쿼리) 
#x1, y1, x2, y2 = querie
#인덱스 리스트 
#rotate 할 리스트 (deque)
#3. deque.rotate()
#가장 작은 거 하나 넣기 
#4. 기존 인덱스리스트를 돌면서 넣기 
#[Output]



# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때,
#  각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# rows는 2 이상 100 이하인 자연수입니다.
# columns는 2 이상 100 이하인 자연수입니다.
# 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
# queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
# queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
# x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
# 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
# 모든 회전은 순서대로 이루어집니다.
# 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.