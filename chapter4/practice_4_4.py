# 집합 (set)
# 중복, 순서 X
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set({"유재석", "박명수"})

# 교집합 (자바와 파이썬 둘 다 가능)
print(java & python)
# print(java.intersection(python))

# 합집합 (자바 또는 파이썬 가능)
print(java | python)
# print(java.union(python))

# 차집합 (자바가 가능한 사람 중 파이썬 가능을 제외)
print(java - python)
# print(java.difference(python))

# 파이썬 하는 사람의 증가
python.add("김태호")
print(python)

# 자바를 잊어버림
java.remove("김태호")
print(java)