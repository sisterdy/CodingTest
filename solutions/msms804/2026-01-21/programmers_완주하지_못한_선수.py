# 일단 각각 소팅, 각각 비교?
# 만약 두 원소가 다르다면 participant에 있는걸 return
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
        
    return participant[-1]
