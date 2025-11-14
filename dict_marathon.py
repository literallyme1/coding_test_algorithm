participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

from collections import Counter

#2일차 풀이 
participant_count = Counter(participant)
completion_count = Counter(completion)

total_count = participant_count - completion_count

print(list(total_count.keys())[0])
#/.







# participant_count = Counter(participant)


# #완주한 사람 count
# for i in completion:
#     participant_count[i] -= 1
#     #완주했다면 지우기 
#     if participant_count[i] == 0:
#         del participant_count[i]


# for i in participant_count.keys():
#     print(i)

# participant_count = Counter(participant)
# completion_count = Counter(completion)

# diff = participant_count - completion_count
# print(list(diff.keys())[0])

# print(type(diff.keys()))




