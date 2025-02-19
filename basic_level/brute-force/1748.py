#백준 1748번 
# URL : https://www.acmicpc.net/problem/1748
#PyPy3 Code

def count_digits(N):
    #총 자리개수 
    digit_count = 0
    # 확인할 자릿수 (1, 10, 100 ...)
    digit_position = 1
    #자릿수의 개수 
    num_length = 1

    #whole 값이 있는 지 확인해야 함. 
    while digit_position * 10 <= N:
        # n 안에 몇 개의 자릿수 개수가 있는 지 파악
        count_in_this_range = digit_position * 9
        #개수 계산 
        digit_count += count_in_this_range * num_length
        #자릿수 증가 
        digit_position *= 10
        #자릿수 개수 증가
        num_length += 1 
    
    # 🔥 마지막 남은 숫자 처리 (N이 속한 자리수)
    digit_count += (N - digit_position + 1) * num_length

    print(digit_count)

#입력 
N = int(input())
count_digits(N)