# 방법 1
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % 'A')
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))  # {} 안에 인덱스가 없으면 순서대로
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))  # 있으면 인덱스 번호로

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))  # 인덱스를 숫자가 아닌 변수처럼 사용 가능
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

# 방법 4 (v 3.6 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
