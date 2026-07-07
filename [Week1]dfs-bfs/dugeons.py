#[state] dfs (묶음)
#[input] k(현재 피로도), dungeons(최소 피로도) ["최소 필요 피로도", "소모 피로도"]
#[logic] main -> for 문 으로 돌아서, 현피 >= 최피면 dfs 실행 
# 종료조건 visited = true, for 문 visited x, 현피, 최피 -> dfs (visited, 던전 인덱스, depth (기본값 = 0 ))
#[output] 최대 던전 수 


maxCount = 0
dungeons = [[80,20],[50,40],[30,10]]
k = 80
n = len(dungeons)
visited = [False] * n

def dfs(count, nHp):
    ans = count 
    
    for i, (mHp, hp) in enumerate(dungeons):

        if nHp >= mHp and not visited[i]:
            visited[i] = True
            ans = max(ans, dfs(count + 1, nHp - hp))
            visited[i] = False
    return ans

dfs(0, k)