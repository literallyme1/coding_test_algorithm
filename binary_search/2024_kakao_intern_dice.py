
from collections import defaultdict
import sys

def solution(dice):
    pick = int(len(dice) / 2)

    # 1. 중복 제외, 모든 숫자 가져오기  
    number = list(set(num for sub in dice for num in sub ))
    
    # 2. 승,패 정보를 담을 딕셔너리 생성
    result = defaultdict(int)

    # 3. 승, 패 비교
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[i] > number[j]:
                result[i] += 1

    #4. 각 다이스의 승률 비교 
    dice_per = defaultdict(int)
    for i, die in enumerate(dice):
        for j in die:
            dice_per[i] += 1

    
    top =  sorted(dice_per.items(), key=lambda x: x[1], reverse=True)[:pick]
    return [idx + 1 for idx, _ in top]


input = eval(input(sys.stdin.readline))
print(solution(input))
