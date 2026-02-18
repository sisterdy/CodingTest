"""
약수 탐색 논리를 사용한 풀이.

전체 면적 S = brown + yellow 이고,
가로 * 세로 = S 를 만족하는 (가로, 세로) 쌍을 찾는다.

즉, S의 약수를 하나씩 탐색하면서
조건을 만족하는 직사각형을 찾는 문제이다.
"""

def solution(brown, yellow):
    S = brown + yellow  # 전체 카펫 면적 (가로 * 세로)
    
    ans = [0, 0]  # [가로, 세로]를 저장할 1차원 리스트

    # 너비(width)를 큰 값부터 탐색
    # 문제 조건상 가로 >= 세로 이므로 큰 값부터 탐색하면
    # 정답을 찾는 즉시 종료 가능
    for width in range(S - 1, 0, -1):
        
        # width가 S의 약수가 아니면
        # 직사각형을 만들 수 없으므로 건너뜀
        if S % width != 0:
            continue
        
        height = S // width  # 세로 길이 계산 (S = width * height)
        
        # 노란 영역은 테두리를 제외한 내부 영역이므로
        # (width - 2) * (height - 2)
        y = (width - 2) * (height - 2)
        
        # 갈색 영역은 전체 면적 - 노란 영역
        b = S - y
        
        # 문제에서 주어진 brown, yellow 값과 일치하면 정답
        if y == yellow and b == brown:
            ans[0] = width
            ans[1] = height
            break  # 정답을 찾았으므로 탐색 종료

    return ans
