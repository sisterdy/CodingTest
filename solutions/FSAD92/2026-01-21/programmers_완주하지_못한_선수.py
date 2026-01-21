"""
배열 participant
배열 completion

단 한 명의 선수를 제외하고는 모든 참가자가 마라톤을 완주했다.
동명이인이 있을 수 있다.
완주하지 못한 선수의 이름을 return

만약 두 배열을 합쳐서 set으로 중복을 모두 없앤다면?
동명이인까지 사라져버리니 이 방법은 안 됨...

예를 들어
leo kiki leo(동명이인)가 참여해서
leo kiki가 완주했다면 
leo만 리턴해야 하는 건데...

저 두 배열을 합치면,
leo kiki leo leo kiki
set으로 중복을 제거하면
leo kiki가 되버리니까 불가.

기존 코드

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    return answer
    

근데 이렇게 하니까 참가자가 1명일 때 케이스를 커버할 수가 없음
왜냐면 문제에서
완주자의 길이는 참가자들의 길이보다 1작다고 했음
즉 참가자가 1일 때는 len(완주자) => 0이 됨

다시 생각해보자

간단하게 이 문제는
completion에는 있고
participant에는 없는 값을 찾는 것

더 간단하게 설명하자면
두 배열을 앞에서부터 가리키는 포인터 두 개를 사용하듯
그 포인터를 하나씩 한 칸씩 옮기며 값을 비교하다가
completion을 기준으로 값이 다른 걸 출력하면 되는 것

"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    # 완주자 목록을 기준으로 순회하며 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            # 중간에 다른 이름이 나오면 그 사람이 미완주자
            return participant[i]
            
    # for문을 다 돌았는데도 미완주자를 못 찾았거나
    # 참가자가 1명이라 루프가 실행되지 않은 경우(completion의 길이는 participant의 길이보다 1 작습니다.)
    return participant[-1]