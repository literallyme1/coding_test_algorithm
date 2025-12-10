
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
    hour, min= map(int, time.split(":"))
    return hour * 60 + min

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
            "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))