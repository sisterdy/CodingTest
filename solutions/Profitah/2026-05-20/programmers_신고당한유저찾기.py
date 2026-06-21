"""
구해야할 것 : id_list 에 입력된 유저가 정지 시킨 (k 회이상 신고한) 유저를 확인하고
내가 정지시킨 유저가 몇명인지 = 각 유저가 몇번 메일을 받았는지

1. report 중복 제거
2. 각 유저가 몇 번 신고당했는지 계산
3. k 이상 신고당한 유저(정지 유저) 찾기
4. report 다시 보면서
   내가 신고한 대상이 정지 유저면
   메일 수 +1


"""
from collections import Counter

def solution(id_list, report, k):
    # 1. 신고당한 횟수 계산
    # report 중복 제거
    report = set(report)

    # 신고당한 횟수 저장 딕셔너리
    reported_count = {user: 0 for user in id_list}

    # 메일 수 저장 딕셔너리
    mail_count = {user: 0 for user in id_list}

    # 신고당한 횟수 계산
    for r in report:
        reporter, reported = r.split()
        reported_count[reported] += 1
        
    # 2. 정지당한 유저 찾기
    banned_users = []
    
    for user in reported_count:
        if reported_count[user] >= k:
            banned_users.append(user)


    # 3. 메일 수 계산
    for r in report:
        reporter, reported = r.split()

        # 신고한 대상이 정지 유저라면
        if reported in banned_users:
            mail_count[reporter] += 1


    # 4. 정답 배열 생성
    answer = []

    for user in id_list:
        answer.append(mail_count[user])

    return answer