"구하고자 하는 것은 숫자를 자르고 난 뒤 K 번째의 수."

def solution(array, commands):

    # answer 배열 생성
    answer = []

# 슬라이싱 범위 설정.
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        
        # 슬라이싱
        slice = array[i-1:j] # 슬라이싱
        slice.sort() # 정렬
        answer.append(slice[k-1]) # 배열에 저장
        
    return answer