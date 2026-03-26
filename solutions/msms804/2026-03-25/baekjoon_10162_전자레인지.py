import sys

# A = 300
# B = 60
# C = 10

# # 최소조작이면 숫자가 큰거부터 나눠가먄 될 듯

# cook_time = int(sys.stdin.readline())
# answer_A = 0
# answer_B = 0
# answer_C = 0

# while cook_time > 0:
#     if cook_time >= A:
#         answer_A += cook_time // A
#         cook_time = cook_time % A
#     elif cook_time >= B:
#         answer_B += cook_time // B
#         cook_time = cook_time % B
#     elif cook_time >= C:
#         answer_C += cook_time // C
#         cook_time = cook_time % C
#     else:
#         print(-1)
#         exit()
#     print(cook_time)

# print(answer_A, answer_B, answer_C) 

cook_time = int(sys.stdin.readline())
answer = []

# 10으로 나누어 떨어지지 않으면 -1
if cook_time % 10 != 0:
    print(-1)
else:
    A = cook_time // 300 
    cook_time %= 300
    
    B = cook_time // 60 
    cook_time %= 60

    C = cook_time // 10

    print(A, B, C)