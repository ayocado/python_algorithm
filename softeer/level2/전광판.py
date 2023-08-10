# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=624&sw_prbl_sbms_sn=248159
# 실행 시간 : 134ms
# 메모리 : 38.4Mb

import sys

T = int(sys.stdin.readline())
tests = [list(map(str, sys.stdin.readline().split())) for _ in range(T)]

switch = {'-1':[], '0':[1, 2, 3, 5, 6, 7], '1':[3, 6], '2':[1, 3, 4, 5, 7], '3':[1, 3, 4, 6, 7], '4':[2, 3, 4, 6], '5':[1, 2, 4, 6, 7], '6':[1, 2, 4, 5, 6, 7], '7':[1, 2, 3, 6], '8':[1, 2, 3, 4, 5, 6, 7], '9':[1, 2, 3, 4, 6, 7]}

for A, B in tests:
    A = ['-1'] * (5 - len(A)) + list(map(str, A))
    B = ['-1'] * (5 - len(B)) + list(map(str, B))
    answer = 0

    for idx, number in enumerate(A):
        switch_A = switch[number]
        switch_B = switch[B[idx]]
        
        for num in range(1, 8):
            if num in switch_A and num not in switch_B:
                answer += 1
            elif num not in switch_A and num in switch_B:
                answer += 1
                
    print(answer)