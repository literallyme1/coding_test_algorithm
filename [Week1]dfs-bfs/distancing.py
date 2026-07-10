#[state]
#[input] places P(person), O(table), X(partition), 5*5
#[logic] 
# 좌표 미로찾기처럼 보면 됨. 
# 갈 수 있는 길, dist 사람 존재 -> 2 내라면 안적음,
# dist 2 일 시 둘 다 안지킴, 적고 둘 다 true -> 시작점은 어떻게 알지?
#[output] result (거리두기 yes 1 or no 0)


# 모든 P를 하나씩 시작점으로 잡고
# 각 P마다 visited를 새로 만들고
# X는 막힌 길로 처리하면서
# 거리 2까지만 BFS 탐색해.
# 그 안에서 다른 P를 만나면 해당 대기실은 0.