"""해시 테이블 구조의 자료구조를 활용하여 문제를 풀이하려 한다.
딕셔너리를 사용해 name, number라는 이름으로 key와 value 값을 쪼개서 넣고.
name:  number number: name 구조의 딕셔너리를 두개 만든다.
이후 번호로 1딕셔너리의 키값을 활용해 2딕셔너리의 value값중 중복값이 있는지 확인한다.

정말 비효율적인 방법인데, 시스터디 친구들이 효율적인 코드를 가져왔으리라 믿는다."""

def solution(phone_book):
    # 전화번호를 key로 빠르게 조회하기 위한 딕셔너리 (해시 테이블)
    phone_dict = {}

    # 모든 전화번호를 딕셔너리에 저장
    for phone in phone_book:
        phone_dict[phone] = 1

    # 각 전화번호에 대해 접두어가 존재하는지 확인
    for phone in phone_book:
        prefix = ""

        # 전화번호를 앞에서부터 한 글자씩 늘려가며 접두어 생성 (1, 11, 119)
        for digit in phone:
            prefix += digit

            # prefix가 딕셔너리에 존재하고,
            # prefix가 자기 자신이 아니라면 접두어 관계 성립
            if prefix in phone_dict and prefix != phone:
                return False

    # 모든 경우를 확인했는데 접두어가 없다면
    return True
