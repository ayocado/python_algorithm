# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=413
# 실행 시간 : 106ms
# 메모리 : 37.3Mb

import sys
N = int(sys.stdin.readline())
split = 1

while N != 0:
    split *= 2
    N -= 1

print((split + 1) ** 2)