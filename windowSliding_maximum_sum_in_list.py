
# ## ------------------ 고정 크기 ------------------

# 정수 배열 a = [1, 12, -5, -6, 50, 3]와 정수 k = 4가 주어진다.
# 길이가 k인 연속 부분배열의 최댓값 합을 구하라.

a = [1, 12, -5, -6, 50, 3]
k = 4

cur = sum( a[:4])
best = cur 

for i in range(4, len(a)):
    cur += a[i]
    cur -= a[i - k]

    best  = max(cur, best)
    
print(best)