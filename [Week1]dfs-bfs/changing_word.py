#[state] dfs
#[input] 
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
#[logic]
#1. zip 이용해서 하나가 다르면 갈 수 있음. for 문 
# 종료 조건 cog or 끝
#for 문 돌면서 dfs , visited -> backtracking 
#[output] 최소 단계 


# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계


