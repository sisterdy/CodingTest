# 문자열로 치환하고 배열의 첫 요소가 가장 큰것을 기준으로 소팅
### !!! 직접 비교 버전도 풀어볼것
def solution(numbers):
    answer = ''
    
    strs = list(map(str, numbers))
    strs.sort(key=lambda x: x * 3, reverse=True)    
    answer = ''.join(strs)
    
    # 만약 [0, 0, 0] 인 경우가 있을 수 있으므로
    return '0' if answer[0] == '0' else answer