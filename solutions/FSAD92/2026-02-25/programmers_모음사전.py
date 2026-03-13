"""
일단 모든 문자를 만들어야 하나?
어떻게 모든 문자를 만들지?
dfs?
"""
def solution(word):
    answer = 0
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(curr_word):
        if len(curr_word) > 5:
            return
    
        if curr_word:
            dictionary.append(curr_word)

        for v in vowels:
            dfs(curr_word + v)
    
    dfs("")
        
    return dictionary.index(word) + 1