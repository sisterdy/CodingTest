"""
[단순 구현]
뭐임 이거 비슷한 문제 어딘가 있었는데
1. 지폐의 가로와 세로가 주어지면 더 긴쪽을 판별.
2. 지갑에 돈이 들어가는지 확인
3. 접을 수 있다면 접고 결과 저장 (홀수라면 소수점 이하는 버림)
4. 90도 돌려서 지갑에 넣을 수 있다면 중지. 
5. 최종결과 출력
"""
def solution(wallet, bill):
    answer = 0

    # 처음부터 들어가면 바로 종료
    if max(bill) <= max(wallet) and min(bill) <= min(wallet):
        return 0

    while True:
        # 1. 더 긴쪽 판별
        if bill[0] >= bill[1]:  # bill[0]이 더 길거나 같음
            long_idx = 0
        else:                   # bill[1]이 더 김
            long_idx = 1

        # 2. 지갑에 돈이 들어가는지 확인
        need_fold = max(bill) > max(wallet) or min(bill) > min(wallet)

        # 3. 돈을 접을 수 있다면 접고 횟수 저장
        if need_fold:
            bill[long_idx] //= 2
            answer += 1

        # 4. 90도 돌려서 지갑에 들어가는지 확인 후 중지
        if max(bill) <= max(wallet) and min(bill) <= min(wallet):
            break

    # 5. 최종결과 출력
    return answer