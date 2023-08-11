# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=584&sw_prbl_sbms_sn=248996
# 실행 시간 : 106ms
# 메모리 : 37.04Mb

import sys

N, M = map(int, sys.stdin.readline().split())

limit_dis = 0
limits = []
for _ in range(N):
    limit = list(map(int, sys.stdin.readline().split()))
    limit_dis += limit[0]
    limits.append([limit_dis, limit[1]])

test_dis = 0
tests = []
for _ in range(M):
    test = list(map(int, sys.stdin.readline().split()))
    test_dis += test[0]
    tests.append([test_dis, test[1]])

limit_idx, test_idx = 0, 0
answer = 0
for dist in range(1, 101):
    if dist > limits[limit_idx][0]:
        limit_idx += 1
    if dist > tests[test_idx][0]:
        test_idx += 1
    if limits[limit_idx][1] < tests[test_idx][1]:
        over = tests[test_idx][1] - limits[limit_idx][1]
        if answer < over:
            answer = over

print(answer)