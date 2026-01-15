import re
#[State]
#[Input]
#[Logic] 새 유저 -> 아이디 규칙 틀림 -> 유사한 아이디 추천
#ID 조건 
# 3<=id <= 15, 문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용가능

def solution(new_id):
#1. 소문자 치환 #2. 숫자, 빼기(-), 밑줄(_), 마침표(.) 제외 제거 
    id = re.sub(r'[^a-z_.-]', '', new_id.lower()) #/ 이것도 어쩔 수 없이 포함되는건가? 

    #3. . 이 연속 2개 -> 하나 치환 / 앞 뒤 . 제거 
    id = re.sub(r'\.{2,}','.', id)
    id = id.strip('.')
    

    #4. 빈문자열 -> a 대입 
    if not id : id = "a"

    #5. 15자 외 다 제외 -> . 이 마지막 위치하는 지 다시 확인 
    id = id[:15]
    id.rstrip('.')

    #6. newId <=2, str + (3- len(newId))* str[-1] 마지막 문자 추가 
    while 3 > len(id):
        id += id[-1]
    #[Output] 추천 아이디를 return
    print(id)
solution("...!@BaT#*..y.abcdefghijklm")