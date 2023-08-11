# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=407&sw_prbl_sbms_sn=249037
# 실행 시간 : 107ms
# 메모리 : 37.41Mb

import sys
K, P, N = map(int, sys.stdin.readline().split())

for i in range(N):
    K = (K * P) % 1000000007

print(K)