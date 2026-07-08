"""
기존 코드는 set으로 각 번호의 접두어를 만들어서 set에 있는지 확인했음
이번에는 접두어 관계라면 정렬했을때 서로 붙어있을 거기 때문에 이 로직으로 풂
"""
def solution(phone_book):
    phone_book.sort()

    # 정렬 후에는 바로 다음 번호만 확인
    for i in range(len(phone_book) - 1):
        current = phone_book[i]
        next_number = phone_book[i + 1]

        # 다음 번호가 현재 번호로 시작하면 현재 번호는 다음 번호의 접두어다.
        if next_number.startswith(current):
            return False

    return True