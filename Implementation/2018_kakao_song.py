#[State]
#[Input] 멜로디를 담은 문자열 m,  방송된 곡의 정보를 담고 있는 배열 musicinfos (100개 이하, 시작, 끝, 제목, 악보 컴마로 구분  )

def normalize(s):
    return s.replace("C#", "c") \
            .replace("D#", "d") \
            .replace("F#", "f") \
            .replace("G#", "g") \
            .replace("A#", "a")

def gap(start, end):
    start_hour, start_min = map(int, start.split(':')) #int 로 변환 방법을 모르겠음. 언패킹 하면 map 요소 x
    start_total = start_hour * 60 + start_min
    end_hour, end_min = map(int, end.split(':'))
    end_total = end_hour * 60 + end_min
    return end_total - start_total

def solution(m, musicinfos):
    song = "(None)" # for 문 밖에 둬야하는 데 안에 둠. 
    total_gap = 0
    for info in musicinfos:
        #1. 컴마로 나누기 -> 갭 시간 구해줌.
        start, end, title, lyl = info.split(',')
        gap_min = gap(start, end)

        #2. # -> 치환 C# -> H, D# -> I,  F# -> J, G# -> K, A# ->L
        lyl = normalize(lyl)
        m = normalize(m)

        #3. 실제 라디오 배열 전체 파악
        if len(lyl) > gap_min:
            lyl = lyl[:gap_min]
        else:
            leak_time = gap_min - len(lyl)
            lyl = lyl + lyl * (leak_time // len(lyl)) + lyl[:(leak_time % len(lyl))]
        #4. in 으로 있는 지 확인 
        if m in lyl:
            # if total ^ -> song 바꾸기, total_time == 0  없을 시 None 
            if total_gap < gap_min :
                song = title
                total_gap = gap_min
    return song

print(solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))