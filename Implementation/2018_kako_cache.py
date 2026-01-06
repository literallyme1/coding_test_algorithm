#[State] deque 
#[Input]  캐시 크기(cacheSize)  0 ≦ cacheSize ≦ 30 와 문자열 배열(cities)  <= 100,000, for 문 대소문자 구분X(toLowerCase)
#[Logic] LRU(Least Recently Used)
#if city in deque
    #yes -> pop 맨뒤로 count +=1
    #no -> 일단 넘어감. 
#len(deque) == cacheSize 확인   
    #yes : count += 5, deque 넣기 
    #no : left_pop , 뒤에 넣기 += 5
# cacheSize == 0 일 때 특수경우 

#[Output]도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력  


