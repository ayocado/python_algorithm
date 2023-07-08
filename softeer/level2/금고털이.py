# 루팡은 배낭을 하나 메고 은행금고에 들어왔다. 금고 안에는 값비싼 금, 은, 백금 등의 귀금속 덩어리가 잔뜩 들어있다. 배낭은 W ㎏까지 담을 수 있다.
# 각 금속의 무게와 무게당 가격이 주어졌을 때 배낭을 채울 수 있는 가장 값비싼 가격은 얼마인가?
# 루팡은 전동톱을 가지고 있으며 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다.

# 실행시간 : 2128ms
# 메모리 : 203.17Mb

import sys
W, N = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
jewels = sorted(jewels, key=lambda x:x[1], reverse=True)
answer = 0

while W > 0:
    for jewel in jewels:
        if jewel[0] <= W:
            answer += jewel[0] * jewel[1]
            W = W - jewel[0]
        else:
            answer += W * jewel[1]
            W = 0

print(answer)