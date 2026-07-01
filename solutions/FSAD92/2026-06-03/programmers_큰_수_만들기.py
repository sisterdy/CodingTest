"""
k개 숫자를 제거했을 때 만들 수 있는 가장 큰 숫자를 string으로 return

스택으로 풀어볼까
작은 숫자를 제거해서 앞자리를 최대한 크게 만들기
현재 숫자가 이전 숫자보다 크면, 이전 숫자를 지우는 게 어쨌든 이득이니까
"""
def solution(number, k):
    answer = []
    cnt = k

    for digit in number:
        while cnt > 0 and answer and answer[-1] < digit:
            answer.pop()
            cnt -= 1

        answer.append(digit)

    # 아직 cnt가 남았다면 뒤에서 제거
    if cnt > 0:
        answer = answer[:-cnt]

    return ''.join(answer)
