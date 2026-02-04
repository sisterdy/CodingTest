from functools import cmp_to_key

def solution(numbers):
    # 정수를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 커스텀 비교 함수: 두 수를 붙여서 비교
    def compare(x, y):
        if x + y > y + x:  # "x"+"y" vs "y"+"x"
            return -1  # x가 앞에
        elif x + y < y + x:
            return 1   # y가 앞에
        else:
            return 0   # 같음
    
    # 정렬
    numbers.sort(key=cmp_to_key(compare))
    
    # 결과 생성
    answer = ''.join(numbers)
    
    # 예외: 모든 숫자가 0인 경우 "0000..." → "0"
    return str(int(answer))

"""
# 3과 30을 비교할 때:
"3" + "30" = "330"
"30" + "3" = "303"
→ "330" > "303"이므로 3이 앞에!

# 3과 34를 비교할 때:
"3" + "34" = "334"
"34" + "3" = "343"
→ "343" > "334"이므로 34가 앞에!
"""