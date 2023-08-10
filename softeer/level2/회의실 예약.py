# 문제 링크 : https://softeer.ai/practice/info.do?idx=1&eid=626&sw_prbl_sbms_sn=248120
# 실행 시간 : 119ms
# 메모리 : 37.42Mb

import sys

N, M = map(int, sys.stdin.readline().split())
rooms = [sys.stdin.readline().rstrip() for _ in range(N)]
rooms.sort()

booking, not_booking = {}, {}
for room in rooms:
    booking[room] = []
    not_booking[room] = []

for _ in range(M):
    arrangement = list(sys.stdin.readline().split())
    booking[arrangement[0]].append([int(arrangement[1]), int(arrangement[2])])
    booking[arrangement[0]].sort()

for room in rooms:
    startTime = 9
    for start, end in booking[room]:
        if start - startTime != 0:
            not_booking[room].append([startTime, start])
        startTime = end
    if startTime != 18:
        not_booking[room].append([startTime, 18])

for room in rooms:
    print('Room ' + room + ':')

    if len(not_booking[room]) == 0:
        print('Not available')
    else:
        print(str(len(not_booking[room])) + ' available:')
        for start, end in not_booking[room]:
            print("{0:>02d}-{1:>02d}".format(start, end))
    
    if room != rooms[-1]:
        print('-----')