# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 변수 내 문자 전체 소문자로
print(python.upper()) # 변수 내 문자 전체 대문자로
print(python[0].isupper()) # 변수 내 0번째가 대문자인지 확인, True/False
print(python[0].islower()) # 변수 내 0번째가 소문자인지 확인
print(len(python)) # 변수 내 몇글자인지
print(python.replace("Python", "Java")) # 변수 내 문자를 변경

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 변수 내 Java 가 없으면 -1 출력.
print(python.index("Java")) # 변수 내 Java 가 없으면 오류 출력

print(python.count("n")) # 변수 내 n이 몇개인지