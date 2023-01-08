customer = "토르"
idx = 5
while idx >=1:
    print(f"{customer}님, 커피가 준비되었습니다. {idx} 번 남았어요")
    idx -= 1
    if idx == 0:
        print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# idx = 1
# while True:
#     print(f"{customer}님, 커피가 준비되었습니다. 호출 {idx}회")
#     idx += 1

customer = "토르"
person = "Unknown"

while person != customer:
    print(f"{customer}님, 커피가 준비 되었습니다")
    person = input("이름이 어떻게 되세요? ")