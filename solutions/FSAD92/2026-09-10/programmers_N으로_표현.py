def solution(N, number):
    # layers[i]에는 N을 정확히 i번 사용해서 만들 수 있는 모든 숫자를 저장
    layers = [set()]

    for used in range(1, 9):
        # 현재 사용 횟수에서 만들 수 있는 숫자들을 저장하는데 중복 방지를 위해 set 도입
        current_layer = set()

        connected_number = int(str(N) * used)
        current_layer.add(connected_number)

        # 현재 사용하는 N의 개수인 used를 두 그룹으로 나누기
        for left_used in range(1, used):
            right_used = used - left_used

            # 그리고 이중 for문으로 조합하기
            for left_value in layers[left_used]:
                for right_value in layers[right_used]:
                    # 사칙연산
                    current_layer.add(left_value + right_value)
                    current_layer.add(left_value - right_value)
                    current_layer.add(left_value * right_value)

                    # UB 방지
                    if right_value != 0:
                        current_layer.add(left_value // right_value)

        if number in current_layer:
            return used

        # 현재 레이어 계산은 끝났으니까 저장 후 다음 레이어에서 활용한다.
        layers.append(current_layer)

    return -1