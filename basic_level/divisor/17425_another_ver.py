#백준 17425번 
# URL : https://www.acmicpc.net/problem/17425
#PyPy3 Code
#누적 히스토그램 처럼 g 만 구하기 
import sys

def calculate_f_g(N_max):

    divisor_sum = [1] * (N_max + 1) #모든 자연수는 1을 약수로 가짐. 
    g_values = [0] * (N_max + 1)
    g_values[1] = 1 

    #약수의 합 f(x) 계산 
    for i in range(2, N_max + 1):
        for multiple in range(1, (N_max // i) + 1):
            divisor_sum[multiple * i] += i # i가 2 일 때, 2*1, 2*2 ...
    
        #누적 합 g(x) 계산 
        g_values[i] = g_values[i - 1] + divisor_sum[i]

    return g_values    

#전부 계산을 해놓음. 
# MAX_VALUE = 1000000
# g_values = calculate_f_g(MAX_VALUE)

#입력 받기 
input = sys.stdin.read
data = list(map(int, input().split()))

MAX_VALUE = max(data)
g_values = calculate_f_g(MAX_VALUE)

#출력 
for i in data[1:]:
    n = int(i)
    print(g_values[n]) 