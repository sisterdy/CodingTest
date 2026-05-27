"""
뭔가 어디선가 풀어본 듯한 기억이 있는데...?
"""
def solution(wallet, bill):
    answer = 0
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer