
#[State] 
#[Input] s, result
#[Logic] 
#1. 이전과 같은 거 prev, curr 
#2. 같으면 +1 다르면 count 있으면 앞에 붙이기 
#[Output] return 압축 문자열 중 가장 짧은 것 

def solution(s):
    n = len(s)
    max = 0 
    for unit in range(1, n // 2 + 1): ##틀린것 1. 범위 + 1 해야함. n//2 까지 포함해야 함. 
        prev = s[:unit]

        #비교를 위한 변수 
        count = 1
        string = ""
        #n칸 비교 
        for j in range(unit, n, unit):
            print(prev)
            curr = s[j:j + unit]
            # print(prev, curr, count)
            if prev == curr:
                count += 1 
            else:## 틀린 것 1. c 를 쓸 수 있는 기회 x (마지막을 어떻게 챙기지? 2c 를 넣을 수 있는 방법)
                if count > 1:
                    string += str(count) + prev
                else:
                    string += prev
                count = 1
                prev = curr
            # 틀린 것 2 : 마지막은 루프 외에서 처리한다. 
            if count > 1:
                string += str(count) + prev
            else:
                string += prev

        
        print(string)
        if len(string) > max:
            max = len(string)
        
    return max



print(solution("aabbaccc"))