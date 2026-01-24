def solution(array, commands):
    answer = []
    for c in commands:
        # c에 대하여 array를 슬라이스
        sliced_array = array[c[0] - 1 : c[1]]
        
        # 슬라이스 한 배열을 정렬
        sliced_array.sort()

        # answer 에 추가
        answer.append(sliced_array[c[2] - 1])
    return answer