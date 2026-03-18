#[State]
#[Input] m(멜로디)	musicinfos (시작한 시각, 끝난 시각  HH:MM 형식 , 음악 제목, 악보 정보)	answer
#[Logic] 
# 처음-끝이 이어졌을 수 0
# 멜로디 -> 재생시간, 악보 대조 
# C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개 (1분에 1개씩 재생)
# 재생시간 > 음악시간 -> 반복
#00:00를 넘겨서까지 재생되지 x
#[Output] 조건 일치 시, 재생 시간이 가장 긴 음악 제목, 재생시간 동일 -> 먼저 입력음악  없을 시 (None) 

def time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    if eh == 0 and em == 0 :
        eh = 24
    start = sh * 60 + sm 
    end = eh * 60 + em 
    return end - start

def normalize(s):
        return s.replace("C#", "c") \
            .replace("D#", "d") \
            .replace("F#", "f") \
            .replace("G#", "g") \
            .replace("A#", "a")
    
def solution(m, musicinfos):
    max_time = 0 
    result = ""
    for info in musicinfos:
        start, end, title, mel =info.split(",")
        interval = time(start, end)

        # 정규화 
        mel = normalize(mel) # 실수 2 , 함수 만들고, normalize x
        m = normalize(m)
        # 재생시간에 맞춰 채우기 
        if len(mel) > interval:
            mel = mel[:interval]
        else: 
            n = interval - len(mel)
            mel = mel + mel[:n]
        #mel 확인 
        if m in mel:
             if interval > max_time:
                  result = title
                  max_time = interval #실수 1 업데이트 x
    return result if not result == "" else "(None)"


print(solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))