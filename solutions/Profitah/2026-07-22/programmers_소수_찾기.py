"""
주어진 숫자들로 만들 수 있는 모든 숫자 중 소수의 개수구하기

---

deque 풀이 -> 없이 풀기
에라토스테네스의 체
주어진 숫자로 만들 수 있는 모든 숫자 중 소수의 개수를 구한다.

---
1.만들 수 있는 숫자를 모두 만든다.
2.가장 큰 숫자까지 소수 여부를 미리 계산한다.
3.만들어진 숫자가 소수인지 배열에서 바로 확인한다.
4.소수의 개수를 센다.


"""



from itertools import permutations

def solution(numbers):

    # 만들 수 있는 모든 숫자 (중복 제거)
    possible_numbers = set()

    # 1자리부터 모든 자리수의 순열 생성 (=모든조합생성)
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            possible_numbers.add(int(''.join(perm)))

    # 생성된 숫자가 하나도 없으면 종료
    if not possible_numbers:
        return 0

    # 만들어진 숫자 중 가장 큰 수
    max_num = max(possible_numbers)

    # !에라토스테네스의 체 (= 소수인지 아닌지 판별하는 배열생성)
    prime = [True] * (max_num + 1)

    # 0과 1은 소수가 아님
    if max_num >= 0:
        prime[0] = False
    if max_num >= 1:
        prime[1] = False

    # 소수가 아닌 수(배수) 제거
    for i in range(2, int(max_num ** 0.5) + 1):
        if prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                prime[multiple] = False

    # 소수 개수 세기
    answer = 0

    for num in possible_numbers:
        if prime[num]:
            answer += 1

    return answer