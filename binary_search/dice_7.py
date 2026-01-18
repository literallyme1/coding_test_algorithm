from itertools import product, combinations

#[State]
#[Input] dice list
#[Logic] 
# 1. a n/2 ->  b n/2 주사위 합 
# index_list = [ i for i in range(len(dices))]
# for a_index in combinations(index_list, n//2)
    #a_dice
    #b_dice = [ not in a_index]

# -> 이길 수 있는 최대 확률의 주사위 
#a, b 가능 리스트 = [add(value) for value in product(*a_dice? )]
#b 리스트 오름차순 sort
#count = 0
#dictionary 
#for i in b_list:
    # dictionary[i]
#[Output] 주사위 번호를 오름차순 return 

from bisect import bisect_left
from collections import defaultdict

def solution(dice):
    max_count = 0 
    max_index = ()
    # 1. a n/2 ->  b n/2 주사위 합 
    index_list = [i for i in range(len(dice))]
    for a_index_list in combinations(index_list, len(index_list) // 2):

        # 1. a n/2 ->  b n/2 주사위 합 
        a_list = [dice[i] for i in a_index_list]
        b_list = [dice[i] for i in index_list if i not in a_index_list] # 빼기로 하면 중복은 다 삭제되나? 

        # 분포 압축
        a_case = {0: 1}
        for one_dice in a_list:
            for i in one_dice:
                for key in a_case.keys():
                    a_case[key + i] += 1

        b_case = {0: 1}     
        for one_dice in b_list:
            temp = defaultdict(int)
            for i in one_dice:
                for key, count in a_case.items():
                    temp[key + i] += count

        #정렬
        b_keys = [ key for key in b_case.keys()].sort()

        #누적합 
        count = 0
        value_list = []
        for key in b_keys:
            count += b_case[key]
            value_list.append(count)
        total_count = 0 
        #bisect
        for key in a_case.keys():
            a_index = bisect_left(b_keys, key)
            if 0 < a_index:
                total_count += value_list[a_index - 1] * a_case[key]
                
        if max_count < total_count:
            max_count = total_count
            max_index = a_index_list
    return sorted(list(max_index))
            





dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))