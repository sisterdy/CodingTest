"""
우리가 구해야 했던 것은
 문자열과 문자열의 사이에 위치해
 길이가 L인 문자열이면 커서가 위치할 수 있는 곳은 L+1가지인 커서의 
위치에 따라 문자열을 조작하고 최종적으로 완성된 문자열을 출력하는 것이었다.
커서 함수를 정의하고,
커서 위치에 따라 문자열을 조작 한 뒤 최종적으로 완성된 문자열을 출력했다.

사용한 자료구조는 스택이다. 
커서 왼쪽 문자열과 커서 오른쪽 문자열을 각각 스택으로 구현해 관리하며, 커서이동과 문자열 처리 과정을 수행했다.

"""

"""
함수정의
"""
import sys
input = sys.stdin.readline # input()은 입력이 끝날 때까지 기다리는 반면, sys.stdin.readline()은 줄 단위로 입력을 받는다. 따라서 입력이 많을 때는 sys.stdin.readline()이 더 빠르다.

# 커서 왼쪽 문자열을 저장하는 리스트와 커서 오른쪽 문자열을 저장하는 리스트
left = list(input().rstrip()) # input()으로 읽으면 줄 끝에 개행문자 \n 가 딸려오고, list로 변환하면 'a', 'b', 'c', 'd', '\n' 이런식으로 저장된다. 따라서 rstrip()으로 개행문자를 제거해주어야 한다.
right = [] # 커서 오른쪽 문자열을 저장하는 리스트

# 명령어를 함수로 정의
def L(cmd): #커서를 왼쪽으로 한 칸 옮기는 함수
    if left: # 커서 왼쪽에 문자가 있다면
        right.append(left.pop()) # 커서 왼쪽에서 마지막 문자를 꺼내서 커서 오른쪽에 추가한다. pop()은 리스트의 마지막 요소를 제거하고 반환하는 메소드이다. 따라서 left.pop()은 left 리스트의 마지막 요소를 제거하고 반환한다. right.append()는 right 리스트의 끝에 요소를 추가하는 메소드이다. 따라서 right.append(left.pop())는 left 리스트의 마지막 요소를 right 리스트의 끝에 추가한다.

def D(cmd): #커서를 오른쪽으로 한 칸 옮기는 함수
    if right: # 커서 오른쪽에 문자가 있다면
        left.append(right.pop()) # 커서 오른쪽에서 마지막 문자를 꺼내서 커서 왼쪽에 추가한다. right.pop()은 right 리스트의 마지막 요소를 제거하고 반환한다. left.append()는 left 리스트의 끝에 요소를 추가하는 메소드이다. 따라서 left.append(right.pop())는 right 리스트의 마지막 요소를 left 리스트의 끝에 추가한다.

def B(cmd): # 커서 왼쪽 문자를 삭제하는 함수 
    if left: # 커서 왼쪽에 문자가 있다면
        left.pop() # 커서 왼쪽에서 마지막 문자를 제거한다. pop()은 리스트의 마지막 요소를 제거하고 반환하는 메소드이다. 따라서 left.pop()은 left 리스트의 마지막 요소를 제거하고 반환한다.

def P(cmd): #커서 위치에 문자를 추가하는 함수
    left.append(cmd[1]) # cmd[1]번째 문자를 커서 왼쪽에 추가한다.

"""
실행문 
"""
n = int(input()) # 명령어의 개수 입력받기
for i in range(n): # n만큼 반복하며 
    cmd = input().split() # 명령어를 입력받고, 공백을 기준으로 리스트로 변환한다.
    
    if cmd[0] == 'L': L(cmd) # cmd[0]이 'L'이라면 L(cmd) 함수를 실행한다.
    elif cmd[0] == 'D': D(cmd) # cmd[0]이 'D'이라면 D(cmd) 함수를 실행한다.
    elif cmd[0] == 'B': B(cmd) # cmd[0]이 'B'이라면 B(cmd) 함수를 실행한다.
    elif cmd[0] == 'P': P(cmd) # cmd[0]이 'P'이라면 P(cmd) 함수를 실행한다.

print(''.join(left + right[::-1])) # right 문자열을 뒤집어서 left 문자열과 합친뒤 출력한다.