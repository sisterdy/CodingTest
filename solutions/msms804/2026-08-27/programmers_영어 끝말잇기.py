# 먼저 탈락하는 사람의 번호, 몇번째 차례에 탈락?
# set로 중복하는지 체크?

def solution(n, words):
    answer = []
    s = {words[0]} # 중복 체크 위해
    
    for i in range(1, len(words)):
        before_word = words[i - 1]
        current_word = words[i]
        
        # 이전 단어의 끝 != 현재 단어의 앞 or 앞에서 말한 단어 있는지 체크
        if (before_word[-1] != current_word[0]) or (current_word in s):
            #  [탈락하는 사람의 번호, 몇번째 탈락]
            return [i % n + 1, i // n + 1]
        
        s.add(current_word) # 검사 끝난 후 추가

    return [0, 0]