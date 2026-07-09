#[state]
#[input] tickets  [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#[logic]
#ICN 출발  
# 한번에 넣고 시작하는게 나을까 vs for 문으로 돌아다니는 게 나을까..(전자가 낫다고 생각)
#1. 딕셔너리, 갈 수 있는 곳 넣고 정렬 
#2. dfs, 처음 나 배열넣기. 
#[output] 방문하는 공항 경로 배열