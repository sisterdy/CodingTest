"""
구해야 하는 것
: 모든 힌트를 만족하는 비밀 코드의 개수

시스템은 1부터 n까지의 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드를 가지고 있다.

비밀 코드를 알아내기 위해 암호 분석 도구를 사용하며, m번의 시도를 할 수 있다.
매번 추측한 숫자 중 실제 비밀 코드와 일치하는 숫자가 몇 개인지만 알 수 있다.

이 정보를 바탕으로, 가능한 비밀 코드의 개수를 구하는 문제이다.

---

1. 가능한 모든 비밀 코드(5개의 조합)를 생성한다.

2. 생성한 비밀 코드 하나를 선택한다.

3. 모든 추측(q)과 비교하여
   공통으로 포함된 숫자의 개수를 구한다.

4. 공통 숫자의 개수가
   문제에서 알려준 ans와 모두 같다면

   → 이 비밀 코드는 가능한 코드이다.

5. 가능한 비밀 코드의 개수를 반환한다.



"""


from itertools import combinations

def solution(n, q, ans):
    # 가능한 비밀 코드의 개수
    answer = 0

    # 1 ~ n 중 5개를 선택하는 모든 비밀 코드 후보 생성
    for secret_code in combinations(range(1, n + 1), 5):

        # 현재 비밀 코드 후보가 모든 힌트를 만족하는지 여부
        is_valid = True

        # 모든 추측 결과와 비교
        for guessed_numbers, matched_count in zip(q, ans):

            # 공통으로 포함된 숫자의 개수 계산
            same_count = len(set(secret_code) & set(guessed_numbers))

            # 힌트와 다르면 해당 후보는 불가능
            if same_count != matched_count:
                is_valid = False
                break

        # 모든 힌트를 만족하면 가능한 비밀 코드
        if is_valid:
            answer += 1

    return answer