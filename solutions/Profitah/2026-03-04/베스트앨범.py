"""
베스트 앨범 문제 (해시 + 정렬)

🎯 우리가 구하는 것
→ 장르별로 가장 많이 재생된 노래를 최대 2개씩 모아
   전체 재생 수가 많은 장르 순으로 인덱스를 반환

📌 핵심 조건
1. 장르별 총 재생 수가 많은 장르부터 수록
2. 각 장르에서는 재생 수가 많은 노래 최대 2개 선택
3. 재생 수가 같다면 고유번호(인덱스)가 낮은 노래 우선

📌 핵심 전략
1. dic1: 장르별 (인덱스, 재생수) 저장
2. dic2: 장르별 총 재생수 저장
3. dic2를 총 재생수 기준 내림차순 정렬
4. 각 장르 안에서 재생수 기준 내림차순 정렬 후 상위 2개 선택

👉 왜 이렇게?
문제의 정렬 기준이
"장르 우선 → 장르 내 재생수 우선"
의 2단계 구조이기 때문
"""

def solution(genres, plays):
    answer = []

    dic1 = {}  # 장르별 (인덱스, 재생수) 리스트 저장
    dic2 = {}  # 장르별 총 재생수 저장

    # 1️⃣ 장르별 정보 수집
    for i, (g, p) in enumerate(zip(genres, plays)):
        # dic1: 장르별 노래 목록 저장
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        # dic2: 장르별 총 재생수 누적
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    # 2️⃣ 총 재생수 기준으로 장르 정렬 (내림차순)
    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):

        # 3️⃣ 해당 장르 내에서 재생수 기준 정렬 후 상위 2개 선택
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer