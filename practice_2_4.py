# 애완동물을 소개해 주세요
animal = "고양이"
name = "해피"
age = 4
hobby = "산책"
is_adult = age >= 3

'''
이렇게 하면
여러 문장을
주석 처리할
수 있습니다
'''

print("우리집 " + animal +  "의 이름은 " + name + "에요")
hobby = "낮잠"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
