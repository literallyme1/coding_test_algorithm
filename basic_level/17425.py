#백준 17425번 
# URL : https://www.acmicpc.net/problem/17425
#PyPy3 Code Code
#각각의 약수 합을 저장해 놓기 (f) + (g)구하기 ver

def calculate_f_g(N_max):

    divisor_sum = [0] * (N_max + 1)
    g_values = [0] * (N_max + 1)

    #약수의 합 f(x) 계산 
    for i in range(1, N_max + 1):
        for j in range(i, N_max + 1, i):
            divisor_sum[j] += i
        #누적 합 g(x) 계산 
        g_values[i] = g_values[i - 1] + divisor_sum[i]

    return g_values    

#T 수만큼 case 받기 
T = int(input().strip())
test_cases = []

for _ in range(T):
    test_cases.append(int(input().strip()))

N_max = max(test_cases)
g_values = calculate_f_g(N_max)

#누적합에서 testCase 만 가져옴. 
results = [g_values[N] for N in test_cases]

#문자열 변경 후, 결과 출력
print("\n".join(map(str, results)))
