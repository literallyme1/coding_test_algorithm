#[state] board
#[input]
#[logic]  "." : blank, "D" : block, "R" : robot, "G" : goal 
# R, G 는 . 으로 봄. 
# 미끄러짐을 어떻게 정의하는가 : 1. 가까운 block 찾기 2. 현재 x 나 y 가 같을 시 -> ( block + 1, -1 가까운데로 이동). 3. 없을 시 0반환 
#dist 넘기기, while 문 -> goal 좌표 일 시 중지 
#[output] 최소 이동 거리 

#1. 하나씩 살피는 게 아니라 쭉 미끄러짐. 
#2. 좌표 -> visited (여러군데 부딪힐 수 있으니.)