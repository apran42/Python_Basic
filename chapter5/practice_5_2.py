'''
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
'''

for waiting_no in range(1, 6):
    print(f"대기번호 : {waiting_no}")

starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print(f"{customer}님, 커피가 준비되었습니다")
