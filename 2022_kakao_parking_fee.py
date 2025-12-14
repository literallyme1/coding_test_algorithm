# 내코드 : 더 짧지만 00:00 시 일 때 오류 발생 가능성 존재 

"""
from collections import defaultdict
import math

def solution(fees, records):

    basic_time, basic_fee, extra_time, extra_fee = fees
    total_fee = []
    #1. records 를 딕셔너리에 넣는다. 
    car_dict = defaultdict(int)
    for record in records:
        time, car_number, in_out_info = record.split()
        if in_out_info == "IN":
            car_dict[car_number] -= change_time_to_min(time)
        else : 
            car_dict[car_number] += change_time_to_min(time)

    car_list = sorted(list(car_dict.keys()))
    print(car_list)
    for car_num in car_list: 

        if car_dict[car_num] <= 0:
            car_dict[car_num] +=  change_time_to_min("23:59")#23:59분 환산 시간 
        #요금 계산 
        #기본 시간만 주차했으면 
        if car_dict[car_num] <= basic_time:
            total_fee.append(basic_fee)
        else :
            total = basic_fee + math.ceil((car_dict[car_num] - basic_time) / extra_time ) * extra_fee
            total_fee.append(total)

    
    #2. key 별 계산, index 2 없을 시 23:59 넣기 
    return total_fee



def change_time_to_min(time):
    hour, minute= map(int, time.split(":"))
    return hour * 60 + minute

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
            "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))

"""

# 리팩토링 버전 : 내 코드는 단기, 특정상황 -> 상태와, 누적합은 분리하는 게 맞다.
import math 
from collections import defaultdict

def solution(fees, records):
    basic_time, basic_fee, extra_time, extra_fee = fees

    # 1. 자료구조 분리
    parking = {}             # 주차 중인 차 (번호: 입차시간)
    total_time = defaultdict(int) # 누적 주차 시간 (번호: 총 분)
    #defaultDict 에 초기값 lamda 지정 가능

    # 2. 기록 순회 
    for record in records:
        time_str, car_num, status = record.split()
        minutes = change_time_to_min(time_str)

        if status == "IN":
            parking[car_num] = minutes
        else: # OUT
            in_time = parking[car_num]
            total_time[car_num] += (minutes - in_time)
            del parking[car_num] # 출차했으므로 목록에서 제거

    # 3. 23:59 정산 (아직 parking에 남아있는 차들)
        end_of_day = change_time_to_min("23:59")
        for car_num, in_time in parking.items():
            total_time[car_num] += (end_of_day - in_time)
    
    # 4. 요금 계산 및 정렬
    answer = []
    # 차 번호 순으로 정렬 (dict.keys() 대신 items() 쓰면 편함)
    for car_num in sorted(total_time.keys()):
        time = total_time[car_num]
        
        # 기본 요금
        if time <= basic_time:
            fee = basic_fee
        # 초과 요금
        else:
            fee = basic_fee + math.ceil((time - basic_time) / extra_time) * extra_fee
        
        answer.append(fee)
        
    return answer

def change_time_to_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m