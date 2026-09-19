"""
[재귀/ 분할정복 ] 쿼드압축 후 개수 세기
- 행과 열로 이루어진 격자 형태의 배열에서 쿼드트리 방식으로 압축할 때
  0의 개수와 1의 개수를 [0의 개수, 1의 개수] 형태로 반환

ex) 
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	result : [4,9]

"""

def solution(arr):
    answer = [0, 0]  # [0의 개수, 1의 개수]
    
    # 영역 압축함수
    def compress(r, c, size):
        # 1. 탐색: 현재 구역이 모두 같은 값인지 확인
        val = arr[r][c] 
        for i in range(r, r + size): # 가로 
            for j in range(c, c + size): #세로
                if arr[i][j] != val: # 탐색하다 현재 i j와 다른 숫자 만나면 압축불가함으로
                    
                    # 2. 분할정복: 4개 구역으로 나눔
                    half = size // 2
                    compress(r,c, half) # 좌상
                    compress(r,c + half, half) #우상
                    compress(r + half, c, half) #좌하
                    compress(r + half, c + half, half) #우하
                    return

        # 3. 재귀 종료: 값이 모두 같으면 카운트
        answer[val] += 1

    compress(0, 0, len(arr))
    return answer