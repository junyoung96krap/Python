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


# 퀴즈) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 -> naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제와 -> naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'의 갯수 + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
url = "http://youtube.com"
# print(url)
my_str = url.replace("http://", "") # 규칙 1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2 my_str 변수 내에서 .위치 직전까지 출력
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙 3
print(password)
