#백준 2309번 
# URL : https://www.acmicpc.net/problem/2309
#PyPy3 Code

import sys 

heights = [int(sys.stdin.readline().strip()) for _ in range(9)]

#전체 키 
total_height = sum(heights)

found = False

for i in range(9): #첫번 째 제외할 난쟁이
    for j in range (i+1, 9):
        if total_height - ( heights[i] + heights[j]) == 100:
            result = [heights[k] for k in range(9) if k !=i and k != j]
            result.sort()
            #출력이 밖으로 가면 result 가 있는 지 확인부터 해야 함. 
            for h in result: 
                print(h)
            
            found = True
            break
    if found:
        break



