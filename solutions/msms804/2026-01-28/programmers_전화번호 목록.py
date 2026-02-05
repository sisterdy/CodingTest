# 2중 for문 으로 다 검사? 시간복잡도 100만 * 100만? -> 안됨
# 정렬, 인접한 것 끼리 비교
### 해시를 이용하는 방법도 해볼것

def solution(phone_book):
    answer = True
    
    # 정렬(문자열 정렬은 사전순)
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        # 그 전의 요소가 다음 번호의 접두어인 경우
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False

    return answer