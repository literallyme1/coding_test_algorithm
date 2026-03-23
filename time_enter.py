import datetime

print("--- [Enter]를 누르면 현재 시간이 출력됩니다 ---")

try:
    while True:
        # 사용자의 입력을 대기합니다.
        input() 
        
        # 현재 시간 가져오기
        now = datetime.datetime.now()
        
        # 밀리초(microsecond의 앞 3자리)까지 포맷팅
        # %f는 마이크로초(6자리)이므로 [:-3]으로 잘라 밀리초로 만듭니다.
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        print(f"현재 시간: {timestamp}")

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")