"""
[문제 설명]
캐릭터는 마음이 약해 공격을 하지 못한다.
그래서 몬스터가 때려도 오직 버텨내기만 한다.

붕대감기 기술로 체력을 회복하면서 몬스터의 공격을 버텨낼 때,
모든 공격이 끝난 후 최종 체력을 구하라. (사망 시 -1 반환)

[구해야 할 것]
모든 공격이 끝난 후의 최종 체력


---

[어떻게 구하는가]
1초씩 시간을 증가시키며 매 초마다 아래 두 가지를 처리
    - 공격 시간이면 → 데미지 적용, 연속 성공 초기화
    - 공격 시간이 아니면 → 초당 회복, t초 연속 성공 시 추가 회복
"""


def solution(bandage, health, attacks):
    # bandage = t (연속 성공 기준 시간)
    # health = x (초당 회복량)
    # attacks = y (연속 성공 시 추가 회복량)

    answer = health  # 현재 체력 = 최대 체력으로 시작
    i = 1            # 현재 시간 (1초부터)
    skill = 0        # 연속 붕대감기 횟수

    while len(attacks) > 0:  # 공격이 남아있는 동안 반복

        if i == attacks[0][0]:       # 현재 시간이 첫 번째 공격 시간과 같으면
            answer -= attacks[0][1]  # 공격 데미지만큼 체력 감소
            skill = 0                # 연속 성공 횟수 초기화
            attacks.pop(0)           # 처리한 공격 제거
            if answer <= 0:          # 체력 0 이하면 사망
                answer = -1
                break

        else:                            # 공격이 없는 시간 = 붕대감기
            answer += bandage[1]         # 초당 회복량 더하기
            if answer >= health:         # 최대 체력 초과 방지
                answer = health
            skill += 1                   # 연속 성공 횟수 +1
            if skill == bandage[0]:      # t초 연속 성공 시
                answer += bandage[2]     # 추가 회복량 더하기
                if answer >= health:     # 최대 체력 초과 방지
                    answer = health
                skill = 0                # 연속 횟수 초기화

        i += 1  # 다음 초로 이동

    return answer