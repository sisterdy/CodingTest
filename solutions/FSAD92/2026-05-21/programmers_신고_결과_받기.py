def solution(id_list, report, k):
    answer = []
    report = set(report)
    report_dict = {user_id: [] for user_id in id_list}  # 각 유저별로 자신이 신고한 사람들의 목록
    reported_count = {user_id: 0 for user_id in id_list}    # 각 유저별로 자신이 신고당한 횟수를 카운트할 딕셔너리
    
    for item in report:
        reporter, reported = item.split()
        report_dict[reporter].append(reported)  # 신고자 처리 목록에 타겟 유저 추가
        reported_count[reported] += 1   # 신고당한 횟수 카운트 1업
        
    # 전체 유저 리스트 순회하며 각자 받을 결과 메일 개수 계산
    for user in id_list:
        mail_count = 0
        
        for target in report_dict[user]:
            if reported_count[target] >= k:     # 선 넘었으면
                mail_count += 1
        answer.append(mail_count)
        
    return answer