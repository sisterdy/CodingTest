"""
입력: brown과 yellow
출력: 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return
가로 길이 >= 세로 길이

yellow의 h(height)를 늘려가면서 대입해보자
"""
def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            line = yellow // i
        
        if (line * 2) + (i * 2) + 4 == brown:
            answer = [line + 2, i + 2]
            break
    return answer