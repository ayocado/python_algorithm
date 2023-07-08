# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=409
# 실행 시간 : 111ms
# 메모리 : 37.16Mb

import sys
N = int(sys.stdin.readline())
blocks = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]
obstacle = 0
obstacle_list = []

for row in range(N):
    for col in range(N):
        if blocks[row][col] == 1 and not visited[row][col]:
            cnt = 1
            obstacle += 1
            visited[row][col] = obstacle
            stack = [[row, col, obstacle]]
            while stack:
                nowRow, nowCol, nowOb = stack.pop()

                for i in range(4):
                    newRow = nowRow + xx[i]
                    newCol = nowCol + yy[i]

                    if 0 <= newRow < N and 0 <= newCol < N and not visited[newRow][newCol]:
                        if blocks[newRow][newCol] == 1:
                            stack.append([newRow, newCol, nowOb])
                            visited[newRow][newCol] = nowOb
                            cnt += 1
                        else:
                            visited[newRow][newCol] = -1
            obstacle_list.append(cnt)

print(len(obstacle_list))
obstacle_list.sort()
print('\n'.join(map(str, obstacle_list)))