#[state] dfs (묶음)
#[input] k(현재 피로도), dungeons(최소 피로도) ["최소 필요 피로도", "소모 피로도"]
#[logic] main -> for 문 으로 돌아서, 현피 >= 최피면 dfs 실행 
# 종료조건 visited = true, for 문 visited x, 현피, 최피 -> dfs (visited, 던전 인덱스, depth (기본값 = 0 ))
#[output] 최대 던전 수 