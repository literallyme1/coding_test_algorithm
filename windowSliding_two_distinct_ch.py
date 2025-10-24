
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
    result = max(result, right - left + 1) #길이

print(result)
