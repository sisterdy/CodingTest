"""
완전탐색 (약수 탐색)

- brown + yellow를 통해 카펫의 전체 넓이를 구한다.
- 가능한 세로 길이(h)를 하나씩 탐색한다.
- 전체 넓이를 h로 나누었을 때 나머지가 0이면:
    → 직사각형 형태가 가능하다는 뜻
- 가로 길이(w)를 계산한다.
- 테두리 1줄을 제외한 내부 크기:
    (w - 2) * (h - 2)
  가 yellow와 같다면 정답이다.

→ 결국 "전체 넓이를 만족하는 직사각형 중,
   내부 노란색 개수가 맞는 경우"를 찾는 문제.
"""

def solution(brown, yellow):
    total = brown + yellow   # 카펫 전체 넓이

    # 가능한 세로 길이 탐색
    for h in range(3, total + 1):

        # 전체 넓이로 직사각형을 만들 수 없는 경우 제외
        if total % h != 0:
            continue

        # 가로 길이 계산
        w = total // h

        # 테두리를 제외한 내부 노란색 개수 확인
        if (w - 2) * (h - 2) == yellow:
            return [w, h]