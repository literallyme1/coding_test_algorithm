"""
Docstring for Implementation.2024_kako_parking_day7
내 의사결정 코드 -> 기획서 같음. 구체적으로. 

##0. input 관리 (split, 시각, 차량번호(길이 4), 내역(in, out)), HH:MM 형식 시간 ->  분단위 숫자 변환 

## 1. 입출 리스트, 차량 요금 딕셔너리 (누적 주차 시간 -> in, out 반복 가능 딕셔너리 합)

## 2. 입출 리스트에 남아있음. -> 출차 : 23:59 -> 정보 습득 

## 3. 계산 (주차 시간 <= 기본 시간 -> 기본 요금 , 기본 요금 + (주차시간 - 기본 시간) / 단위 시간 * 단위 요금)
## 4. 나누어 안떨어지면 ceil()
## 5. 작은 순 리스트 반환 
"""

"""
1. [State] 자료구조 & 변수 정의 
- InMap : <차, 입차시간> -> Map (Hash)가 더 빠름. 
- AccMap : <차, 누적분> (누적 필수
- `fee`: int[] fees
)
2. [Input] 전처리 (파싱, 정렬) 
- getTime 함수 : HH*60  + MM로 변환 
- records 배열 순회하며 공백 Split.

3. [Logic] 핵심 알고리즘 흐름
- 정보 모으기 루프 
- IF IN : inMap.put(번호, 시각)
- ELSE OUT : 
    inTime = inMap.remove(번호)
    accTimemap = `(toMin(시각) - inTime)` 더하기
- 남은 차 처리 
    - `inMap`에 남은 키들 순회
  - `(23:59 - inTime)` 계산해서 `accTimeMap`에 추가

4. [Output] 결과 반환 형식
- carList`: `accTimeMap.keySet()` 꺼내서 **오름차순 정렬**
- 요금 계산 
- 시간 <= 기본: `기본요금`
  - 시간 > 기본: `기본 + Math.ceil((시간-기본)/단위) * 단위요금` (double 이어야 ceil 가능)
"""
from collections import defaultdict
import math

def getTime(time):
  hour, min = map(int, time.split(":"))
  return hour * 60 + min


def solution(fees, records):
  inMap = defaultdict(int)
  accMap = defaultdict(int)

  #1. record 전처리 후 정보 입력 
  for record in records:
      time, car_num, type = record.split()
      time = getTime(time)

      if type == "IN":   
        inMap[car_num] = time
      else:
          in_time = inMap[car_num]
          total = time - in_time
          accMap[car_num] += total 
          del inMap[car_num]
  
  #2. 남은 차 계산
  last_time = getTime("23:59")
  for key in inMap.keys():
      accMap[key] += (last_time - inMap[key])
  
  #3. 요금 계산 
  basic_time, basic_fee, over_min, over_fee = fees
  total_fees = []
  all_car = sorted(set(accMap.keys()))
  for car in all_car:
      if accMap[car] <= basic_time:
          total_fees.append(basic_fee)
      else:
          total_fees.append(basic_fee + math.ceil((accMap[car] - basic_time) / over_min) * over_fee)
  return total_fees
          
      

    
print(solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))