"""
어떤 자연수의 생성자 candidate_number
어떤 자연수 = candidate_number + (candidate_number의 각 자리수 합)
"""
N = int(input())
answer = 0

def get_digit_sum(number):    # 매개변수의 각 자리수 합을 반환하는 함수
    total = 0
    for ch in str(number):
        total += int(ch)
    return total

for candidate_number in range(1, N):
    temp = candidate_number + get_digit_sum(candidate_number)

    if temp == N:
        answer = candidate_number
        break

print(answer)