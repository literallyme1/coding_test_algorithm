#[State]
#[Input] dice
#[Logic]

#1. for 주사위 나누기 (인덱스, combination)
#2. 각각 가능한 주사위 합 (defaultDict, product)
#3. b_dice sort, 횟수 누적합 구하기 
#4. a_dice 각각 bisect_left() if idx > 0, 누적횟수 * 자기 횟수 
#5. total 비교 (반복), 해당 주사위 인덱스 저장 

#[Output] return total, +1 인덱스 

from collections import defaultdict
from itertools import combinations ##itertools 까먹음. 
from bisect import bisect_left
def solution(dice):
    #1. for 주사위 나누기 (인덱스, combination)
    n = len(dice)
    max_total = 0
    index_list = [i for i in range(n)]
    for a_index in combinations(index_list, n // 2):
        a_list = [dice[i] for i in a_index]
        b_list = [dice[i] for i in index_list if i not in a_index]

        #2. 각각 가능한 주사위 합 (defaultDict, product)
        #product x -> tuple 로 나옴. 다시 전처리 
        a_sum = {0 : 1}     
         #dice 개수가 작아서 삼중 포문이 가능할 거라 판단 
        for d in a_list:
            
            for key in a_sum.keys():
                for i in d: 
                    a_sum[key + i] += 1
        b_sum = {0 : 0} #dice 개수가 작아서 삼중 포문이 가능할 거라 판단 
        b_keys = sorted(b_sum.keys())
        sum_list = []
        running = 0
        for key in b_keys:
            running += b_sum[key]
            sum_list.append(running)
        
        #3. 누적합
        b_keys = list(b_sum.keys()).sort()
        a_keys = list(a_sum.keys())

        sum = 0
        sum_list = []
        for key in b_keys:
            sum += b_sum[key]
            sum_list.append(sum)

        #4. b_dice sort, 횟수 누적합 구하기

        total = 0
        for key in a_keys:
            idx = bisect_left(key, b_keys)
            if idx > 0 :
                total += sum_list[idx-1] * a_sum[idx-1]
        if total > max_total:
            max_total = total
    return total




    


