#[State]
#[Input]
#[Logic]

#1. 주사위 나누기 (인덱스)
# n  len(dice)
# index_list  ［i for i in range(n)］
# combination(n//2)

#a_dice, b dice 

# from collections import defaultDict

# 모든 경우의 수 -> dict
#a, b for num in product(a_dice): dict[sum(num)] 

# b_dict.keys().sort()

#3. sorted_key 별 누적합 
# for 문 sum_list.append(n + value)

#4. bisect_left()  if 값 >= 0 : n-1 값 가져오기 total 경우