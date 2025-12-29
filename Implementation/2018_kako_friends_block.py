#[State] 2차원 배열,
#[Input] 길이 n, 문자열 m개, n*m 배열, 
#[Logic]
#1. 4개 얻었는 지 확인 : 2*2 window = [(i,y),(i,y+1),(i ,y),(i+1,y)]
#    2중 포문 for i in range(n-1): for y in range(m-1)
# 기록 list 넣고 set 으로 변경. 1차 끝 total_count += len(set_list)
#2. 지우기 ( set 에 있는 곳 0으로 변경, 같은 인덱스(끝부터 0이 된 인덱스에 자기껄 옮기고, 자신이 0)) -> 함수화
# 2-1. for i in set(인덱스) -> board를 0 변경 2-2. reverse = board.sorted(-1) for string in reverse: 가지고 오기 -> 0 다시 역 
#3. 1-2 반복,, 언제까지 (while true ,window_list 가 훑은 후에 0일시 종료)
 
#[Output] 지워지는 블록은 모두 몇 개

