#[state]
#[input] orders, course (조합 메뉴 개수)
#[logic] 메뉴 조합, 가장 많이 주문한 단품 , 
# 메뉴 : 총 2가지 이상, 2명 이상 손님한테 주문된 것 포함 
#[output] result(사전 순으로 오름차순 정렬)


# [입출력 예]
# orders	course	result
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]

#1. 처음에 1 이하를 제거하고 시작할까? 
#2. set 에 조합된 거 제외, 하나씩 돌려봄. 있는 지 확인, 다른데서 발견, result 에 놓기 
#3. course 에 따라서 반복 (dfs를 이용안해도 될 거 같은데.. 조합해주는 함수 이용..)