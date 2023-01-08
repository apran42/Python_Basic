'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탐 승색 수를 구하는 프로그램을 작성하시오.

조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
'''

from random import *

passenger = [randint(5, 51) for i in range(50)]

cnt = 0

for i in range(len(passenger)):
    if 5 <= passenger[i] <= 15:
        cnt += 1
        print(f"[O] {i+1}번째 손님 (소요시간 : {passenger[i]}분)")
    else:
        print(f"[ ] {i + 1}번째 손님 (소요시간 : {passenger[i]}분)")

print(f"총 탐승 승객 : {cnt}분")