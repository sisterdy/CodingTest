"""
이딴 게 DP...?

일단 N으로 시작한다.
N에 N을 붙여 NN으로 만들거나, NNN으로 만들거나...
사칙연산을 추가한다. 2 +, 2 -, 2 *, 2 -
이런 식으로 모든 경우의 수를 구한다.
근데 이렇게 하면 경우의 수가 너무 많아지지 않나?
뭔가 근사값을 먼저 구하는 로직을 찾아내야 하지 않나?

근데 최솟값이 8보다 크면 -1을 리턴하라고 했으니까 생각보다 경우의 수가 엄청 많아지지는 않겠구나
어쨌든 모든 경우의 수를 찾아봐야겠네
하나 하나 붙여가면서 해야 할테니 바텀업으로 풀어보자
"""
def solution(N, number):
    # N을 i번 사용해서 만들 수 있는 숫자들 dp 테이블 초기화
    # 1번부터 8번까지 필요함. 최솟값이 8보다 크면 -1을 return 해야 하기 때문.
    sets = []
    for _ in range(9):
        sets.append(set())  # 중복 방지 위해 set로 저장
    
    # N을 i번 이어 붙인 숫자(5, 55, ...)를 해당 집합에 추가해놓는다.
    for i in range(1, 9):
        basic_num = int(str(N) * i)
        sets[i].add(basic_num)
        
        # i개의 N을 쓰는 경우를 둘로 쪼개기
        # N을 i번 사용해서 만들 수 있는 모든 경우의 수 계산
        # 여기서 3중 for문을 쓰는데
        # 그 이유는 i가 3일 경우 i=1 집합 + i=2 집합, i=2 집합 + i=1 집합처럼 이전에 저장해놓은 경우의 수들을 조합해야 하기 때문
        for j in range(1, i):
            for num1 in sets[j]:
                for num2 in sets[i - j]:
                    # 사칙연산 수행 후 결과 집합에 add
                    sets[i].add(num1 + num2)
                    sets[i].add(num1 - num2)
                    sets[i].add(num1 * num2)
                    if num2 != 0:   # 0으로 나누기 방지
                        sets[i].add(num1 // num2)
                        
        if number in sets[i]:
            return i
        
    return -1