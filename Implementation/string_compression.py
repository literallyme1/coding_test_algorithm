#[State]
#[Input] s 
#[Logic] n 개 압축 중 가장 짧은 것. 

# 완전탐색: 크기가 작음, 깊게 생각 X, 직관적인 방법 
# 항상 같은 길이여야 함을 간과

# 자리수 탐색 1 ~ (len(s)//n)
#prev, compressed = "", count
# for 문 
# 1. curr 만들어서 , prev 비교 if same -> count + 1 or 적고 -> curr = prev 
#  min compressed

def solution(s):
    result = len(s)
    for unit in range(1, len(s)//2):
        compressed = ""
        prev = s[:unit]
        count = 1 ## 틀린 것
        for i in range(unit, len(s), unit):
            curr = s[i:i+unit]


            if curr == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = curr
                count += 1
            # 계속 hit 였을 시 
            if count > 1:
                compressed += str(count) + prev
            else:
                compressed += prev
        
        
        result = min(result, len(compressed))
    return result