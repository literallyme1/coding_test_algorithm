
#1번 : 삼각형 타일 2번 : 위 -> 역 삼각형 마름모, 3번 역 -> 위 삼각형, 4번 top 마름모 
def solution(n, tops):
    MOD = 10007

    #a[k] = k 번째 삼각형을 3번 타일로 끝내는 방법 수 
    #b[k] = k 번째 삼각형을 3번 외 타일로 끝내는 방법 수 
    a = [0] * (n + 1) #DP 는 1부터 시작, n+1
    b = [0] * (n + 1)


    a[1] = 1 #오직 3번 경우의 수 1
    b[1] = 3 if tops[0] == 1 else 2     

    for k in range(2, n+1):
        a[k] = (a[k-1] + b[k-1]) % MOD

        if tops[k-1] == 1: #tops 는 1부터 시작
            b[k] = (2*a[k-1] + 3*b[k-1]) % MOD
        else:
            b[k] = (a[k-1] + 2*b[k-1]) % MOD
    return (a[n] + b[n]) % MOD #(a + b) % mod = ((a % mod) + (b % mod)) % mod