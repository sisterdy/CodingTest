"""
뭔가 비슷한 문제를 본 것 같은데...
근데 dfs 같은 문제가 아니라 그냥 시뮬레이션 느낌?

딕셔너리에 등장 단어, 등장 순서를 쌍으로 저장하고 관리한 다음에 매번 검사시키는 식?
"""
def solution(n, words):
    # key: 등장 단어, value: 등장 순서 인덱스
    used_words = {}

    for i, word in enumerate(words):
        # 끝말잇기 규칙 체크
        if i > 0 and words[i - 1][-1] != word[0]:
            person = i % n + 1  # 누구 차례인지
            turn = i // n + 1   # 몇 번째 차례인지
            return [person, turn]

        # 이전에 등장한 단어면 탈락
        if word in used_words:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]

        # 처음 나온 단어 -> 최초 등장 위치 저장
        used_words[word] = i

    return [0, 0]