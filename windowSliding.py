
## ------------------ 가변 크기 -------------------

# 문자열 s = "eceba"가 주어진다.
# 서로 다른 문자가 2개 이하인 가장 긴 부분문자열의 길이를 구하라.

from collections import defaultdict

s = "eceba"
dic = defaultdict(int)
left = 0
result = 0

for right, ch in enumerate(s):
    dic[ch] += 1
    while len(dic) > 2:
        dic[s[left]] -= 1
        if dic[s[left]] == 0:
            del dic[s[left]]
        left += 1
    result = max(result, right - left + 1)

print(result)




    



# ## ------------------ 고정 크기 ------------------

# 정수 배열 a = [1, 12, -5, -6, 50, 3]와 정수 k = 4가 주어진다.
# 길이가 k인 연속 부분배열의 최댓값 합을 구하라.

# a = [1, 12, -5, -6, 50, 3]
# k = 4

# cur = sum( a[:4])
# best = cur 

# for i in range(4, len(a)):
#     cur += a[i]
#     cur -= a[i - k]

#     best  = max(cur, best)
    
# print(best)