"""
의사코드...
w를 순회하면서 일단 u,v를 분리해야겠다.
u의 첫 번째 원소가 '('면 올바른 괄호 문자열이므로 이에 따라 분기
"""
def solution(p):
    def split_balanced(w):
        balance = 0

        for i in range(len(w)):
            if w[i] == '(':
                balance += 1
            else:
                balance -= 1

            # balance가 0 => 더 이상 쪼갤 수 없는 균형잡힌 문자열 u의 끝
            if balance == 0:
                return w[:i + 1], w[i + 1:]

    def reverse_brackets(w):
        result = []

        for ch in w:
            if ch == '(':
                result.append(')')
            else:
                result.append('(')

        return ''.join(result)

    def convert(w):
        # 빈 문자열이므로 그대로 반환
        if w == "":
            return ""

        # w를 균형잡힌 문자열 u,v로 분리
        u, v = split_balanced(w)

        # u가 올바른 괄호 문자열인 경우
        if u[0] == '(':
            return u + convert(v)

        # u가 올바른 괄호 문자열이 아닌 경우
        center = u[1:-1]
        reversed_center = reverse_brackets(center)

        return '(' + convert(v) + ')' + reversed_center

    return convert(p)