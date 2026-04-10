import sys

X = sys.stdin.readline()

if X[:2] == "0x": # 16진수
    print(int(X, 16))
elif X[0] == "0": # 8진수
    print(int(X, 8))
else: # 10진수인 경우
    print(int(X))