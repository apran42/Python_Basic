cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 존재하지 않는 key를 호출하면 오류 발생
print(cabinet.get(5))  # 존재하지 않는 key를 호출하면 'None' 출력
print(cabinet.get(5, "사용 가능"))  # 'None' 대신 다른 값 설정 가능

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)