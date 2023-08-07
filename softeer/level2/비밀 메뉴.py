# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=623&sw_prbl_sbms_sn=245873
# 실행 시간 : 110ms
# 메모리 : 37.43Mb

import sys
M, N, K = sys.stdin.readline().split()
recipe = ''.join(list(sys.stdin.readline().split()))
user = ''.join(list(sys.stdin.readline().split()))

if recipe in user:
    print('secret')
else:
    print('normal')