"""

"구하고자 하는 것은 숫자를 자르고 난 뒤 K 번째의 수."

commands는 인덱스 번호가 아닌 차례를 표기함.

commands : [2,5,3]
2 : 여기서 부터 자르세요
5: 여기까지 자르세요
3: 자르고 난 뒤 정렬했을 때 3번째 순서에 있는 숫자를 구하세요.

return : 5

"""

def solution(array, commands):

    # answer 배열 생성
    answer = []

# 슬라이싱 범위 설정.
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        
        # 슬라이싱
        slice = array[i-1:j] # 인덱스 번호를 고려하며 슬라이싱
        slice.sort() # 정렬
        answer.append(slice[k-1]) # 배열에 저장
        
    return answer