# 튜플은 리스트와 달리 수정 불가
# but, 속도는 튜플 < 리스트

menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# menu.add("생선가스")    # 값 추가 불가

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
# (name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
