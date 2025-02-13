#백준 1476번 
# URL : https://www.acmicpc.net/problem/1476
#PyPy3 Code

#(의사코드 1) 입력 
E, S, M = map(int, input().split())

year = 1 #연도 초기화 

#(의사코드 2) 년도를 추가하면서 완전탐색
while True:
    #값이 입력 년도와 일치 하는 지 확인
    # 원하는 값 (ex. (15 -1) % 15 + 1 = 15
    if (year - 1) % 15 + 1 == E and (year - 1) % 28 + 1 == S and (year -1) % 19 + 1 == M:
        print(year)
        break
    year += 1