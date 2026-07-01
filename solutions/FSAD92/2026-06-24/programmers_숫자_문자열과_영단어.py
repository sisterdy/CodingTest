"""
숫자의 일부 자릿수를 영단어로 바꾼 입력 s가 매개변수로 들어옴
s가 의미하는 원래 숫자를 찾아라

origin_num이라는 스택을 하나 만들자
s를 순회하는데 if문을 쫘르륵 만들어서
s[i]이 o면 'one', 즉 i += 3을 해서 인덱스를 건너뛰자. 
"""
def solution(s):
    origin_num = []
    i = 0

    while i < len(s):
        ch = s[i]

        if ch.isdigit():
            origin_num.append(ch)
            i += 1

        elif ch == 'z':
            origin_num.append('0')
            i += 4

        elif ch == 'o':
            origin_num.append('1')
            i += 3

        elif ch == 't':
            if s.startswith('two', i):
                origin_num.append('2')
                i += 3
            else:
                origin_num.append('3')
                i += 5

        elif ch == 'f':
            if s.startswith('four', i):
                origin_num.append('4')
                i += 4
            else:
                origin_num.append('5')
                i += 4

        elif ch == 's':
            if s.startswith('six', i):
                origin_num.append('6')
                i += 3
            else:
                origin_num.append('7')
                i += 5

        elif ch == 'e':
            origin_num.append('8')
            i += 5

        elif ch == 'n':
            origin_num.append('9')
            i += 4

    return int(''.join(origin_num))
