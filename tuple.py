# 튜플 자료형
# 튜플(tuple)은 목록과 유사하지만 몇 가지 중요한 차이점이 있는 내장 Python 데이터 구조입니다. 튜플은 둥근 ​​괄호(소괄호)로 묶인 정렬되고 변경할 수 없는 요소 모음입니다. 튜플의 요소는 다른 튜플, 목록 또는 사전을 포함하여 다양한 데이터 유형일 수 있습니다.
# 변경되지 않는 목록에 주로 사용

menu = ("돈까스", "치즈까스")
print(menu[1])
print(menu[0])

name = "박준영"
age = 31
hobby = "축구"
print(name, age, hobby)

(name, age, hobby) = ("박준영", 31, "축구")
print(name, age, hobby)