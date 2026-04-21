"""
cards 중에 상근이가 갖고 있는 카드가 있는지를 확인하는 프로그램
cards를 딕셔너리로 만들까
"""
import sys
N = sys.stdin.readline().strip()
his = list(map(int, sys.stdin.readline().split(' ')))
M = sys.stdin.readline().strip()
cards = list(map(int, sys.stdin.readline().split(' ')))

cards_dict = {}
for card in cards:
    cards_dict[card] = 0

for card in his:
    if card in cards_dict:
        cards_dict[card] = 1

print(*cards_dict.values())