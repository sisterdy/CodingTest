# 정렬..?
# 어떻게 해야 보트수가 가장 적을까? -> 가장 무거운 사람을 가장 가벼운 사람과 매칭
# 투포인터

def solution(people, limit):
    answer = 0
    people.sort()
    
    
    l = 0                   # 가장 가벼운 사람   
    r = len(people) - 1     # 가장 무거운 사람 
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        answer += 1
                    
    return answer