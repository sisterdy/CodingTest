"""
DFS? 백트래킹? 서로 다른 한 자릿수

'부등호 관계를 만족시키는 정수' -> 하나 이상 존재함
모든 입력에 답은 항상 존재한다는 걸 보면 어쩌구 저쩌구 정수는 2개 이상을 만족하는 입력만 들어오나 본데?

최댓값과 최솟값을 찾아서 출력하는데, 출력 정수는 하나의 '문자열'

dfs 함수의 매개변수는(visited, string_stack)

현재 문자열의 길이가 0일 때는 문자 1개를 string_stack에 추가하고 visited에 방문 체크를 한다.
문자열의 길이 = string_stack의 크기이므로 1로 증가하게 된다.

다음 dfs 진입을 위해 선택한 문자 1개를 제외한 후보 중 하나를 고르는데
먼저, braces[i]가 > 냐 <냐로 분기로 나뉜 후에 가지 치기를 한다.
이 때, 인덱스 i = 현재 문자열의 길이 - 1

예시 1에서 0을 먼저 골랐다고 가정.
braces[i] == '<' 이므로

0을 제외한 숫자 중에서, 0보다 큰 숫자에 한해서만 dfs를 들어간다.
"""
import sys

k = int(sys.stdin.readline())   # 부등호 문자의 갯수
braces = sys.stdin.readline().split()

string_stack = list()  # 문자열
results = []

visited = [False] * 10

def dfs(visited, string_stack):
    if len(string_stack) == k + 1:
        results.append("".join(map(str, string_stack)))
        return
    
    # 문자열 길이가 1일 때(첫 번째 숫자 고르기)
    if len(string_stack) == 0:
        for num in range(10):
            visited[num] = True
            string_stack.append(num)
            dfs(visited, string_stack)
            string_stack.pop()
            visited[num] = False

    # 문자열의 길이가 2 이상일 때(다음 숫자 고르기)
    else:
        i = len(string_stack) - 1
        prev_num = string_stack[-1] # 직전에 고른 숫자

        for next_num in range(10):
            if not visited[next_num]:
                if braces[i] == '<':
                    if prev_num < next_num:
                        visited[next_num] = True
                        string_stack.append(next_num)
                        dfs(visited, string_stack)
                        string_stack.pop()
                        visited[next_num] = False

                elif braces[i] == '>':
                    if prev_num > next_num:
                        visited[next_num] = True
                        string_stack.append(next_num)
                        dfs(visited, string_stack)
                        string_stack.pop()
                        visited[next_num] = False

dfs(visited, string_stack)
print(results[-1])
print(results[0])