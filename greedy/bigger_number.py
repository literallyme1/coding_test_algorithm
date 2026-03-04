
#[State]
#[Input] number(string), k : 제거 개수 
#[Logic] #window 중 가장 큰 수 파악
#[Output] 가장 큰수 return 


#[wrong_understand]
# def solution(number, k):
#     n = len(number)
#     window = n - k
#     loop_num = n - (window - 1)

#     max = 0
#     for idx in range(0, loop_num):
#         start = idx
#         end = idx + window
#         if int(number[start: end]) > max:
#             max = int(number[start: end])
#     return str(max)

# print(solution("1924",	2))


def solution(number, k):
    n = len(number)
    left = n - k
    result = []
    for _ in range(0, left):
        max_num = max(number)
        result.append(max_num)
        max_idx = number.index(max_num)
        number = number[max_idx + 1 : ]
    return "".join(result)
print(solution("1924",	2))