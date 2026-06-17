#[state]
#[input] maps
#[logic] #상, 하, 좌, 우 , 값 = 식량 day 
# 지낼 곳 없으면 -1 
#[output] result # 오름차순, 섬 별 식량 

x = [0, 0, -1, +1]
y = [-1, +1, 0, 0]

# dfs 밖에서 돌리기 
#  x 가 아닐 시 , true 여부 확인  -> true , 상하좌우 dfs 
# 1. visited 필요 -> X 는 True 처리 