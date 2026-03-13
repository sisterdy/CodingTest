"""
예시에 29가 없는 걸 보니 만들 수 있는 모든 경우의 수를 만드는 건 아닌 듯

근데 어떻게 number 숫자에서 k개의 수만큼 제거하지?
문자열을 순회하며 리스트에 넣어야 할까?

그러기엔 number가 너무 크다
슬라이딩 윈도우?
"""
from collections import deque

def solution(number, k):
    n = len(number)
    need = n - k
    left = 0        # 윈도우 시작 인덱스
    right = 0       # deque에 후보를 넣어둔 마지막 + 1 위치
    dq = deque()    # 윈도우 안에서 최댓값 후보 인덱스들을 저장. number[dq[0]]이 현재 윈도우의 최댓값이 되도록 유지
    answer = []
    
    # 첫 자리 선택을 위한 초기 윈도우 채우기
    # 첫 자리는 [0 ... k], 즉 k+1개 범위 중에서 골라야 함
    while right < n and right <= k:
        while dq and number[dq[-1]] < number[right]: dq.pop()   # 새로 들어올 number[right]가 더 크면 상식적으로 덱 뒤쪽의 작은 후보들은 앞으로도 절대 최댓값이 될 수 없으니 제거
        dq.append(right)    # 현재 인덱스를 최댓값 후보로 등록
        right += 1          # 다음 인덱스로 확장

    while need:     # n-k개 뽑으면 완료
        while dq[0] < left:     # deque 맨 앞이 윈도우 밖이면 선택 불가하므로 버림
            dq.popleft()
            
        pick = dq[0]    # 현재 윈도우에서 최댓값 숫자의 인덱스
        answer.append(number[pick])     # 그 숫자를 이번 자리로 확정
        
        k -= pick - left    # left ~ pick - 1 까지는 pick을 고르려고 삭제한 숫자들이므로 그 개수만큼 k 감소
        
        left = pick + 1     # 윈도우 시작 위치 재조정
        need -= 1   # 한 자리 확정했으니 남은 자리 수 감소
        
        if k == 0:  # 더 이상 삭제할 수 없으면
            answer.append(number[left:])    # 남은 부분은 그대로 붙이고 break
            break
            
        while right < n and right <= left + k:  # 다음 자리 선택을 위해 윈도우를 [left ... left + k]까지 확장하면서 후보 추가
            while dq and number[dq[-1]] < number[right]:
                dq.pop()    # 새로 들어오는 숫자가 크면 이번에도 작은 후보들은 제거
            dq.append(right)    # 후보 등록
            right += 1          # 계속 확장

    return ''.join(answer)