"""
start, stop, nth
for문에서 2차원 배열의 원소를 순회할 때마다 초기화될 수 있는 배열을 만들어야 할 거 같은데...

더 간단하게 코드를 짤 수 있을 것 같지만 그건 시스터디 아가들을 믿어보자
"""

def solution(array, commands):
    answer = []
    
    for start, stop, nth in commands:
        sliced = array[start-1:stop]    # 1. start번째부터 stop번째까지 자르고
        sorted_sliced = sorted(sliced)  # 2. 1에서 나온 배열을 정렬하고
        picked = sorted_sliced[nth - 1]   # 3. 2에서 나온 배열의 nth번째 숫자를
        answer.append(picked)   # 4. 정답 리스트에 등록한다
        
    return answer
