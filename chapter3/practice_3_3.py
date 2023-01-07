python = "Python is Amazing"

print(python.lower())  # lower : 모든 문자를 소문자로
print(python.upper())  # upper : 모든 문자를 대문자로
print(python[0].isupper())  # isupper : 문자가 대문자인가
print(len(python))  # len(str) : 문자열의 길이
print(python.replace("Python", "Java"))  # replace(str, str) : 문자열에서 앞의 문자열을 뒤의 문자열로 대체

index = python.index("n")  # index(str) : 문자열이 등장하는 첫번째 인덱스 값 반환
print(index)

index = python.index("n", index + 1)  # index(str, index+1) : 문자열이 등장하는 두번째 인덱스 값 반환
print(index)

print(python.find("Java"))  # find : 원하는 문자열이 없으면 -1을 반환
# print(python.index("Java"))  # index : 원하는 문자열이 없으면 오류 발생
print(python.count("n"))    # count : 문자열에서 'n'이 등장하는 횟수
