# 숫자 자료형

print(5)
print(-10)
print(3.14)
print(1000)
print(5-3)
print(2*8)
print(3*(3+1))

# 문자 자료형

print('풍선')
print("나비")
print("ㅋ"*9)

# boolean 자료형 (참 / 거짓)

print(5 < 2)
print(5 > 2)
print(True)
print(False)
print(not True)
print(not (5 > 10))

# 변수 

# 애완동물을 소개해주세요~
# str 정수형을 문자형으로 변경

animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의이름은 " + name + "이예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며 " + hobby + "을 아주 좋아해요..")
print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아해요..")
print(name + "는 어른일까요?" + str(is_adult))

# 주석 전체 처리

# 여러 문장 선택 
# ctrl + /


# 퀴즈) 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 
# : station
# 변수값
# : 사당, 신도림, 인천공항 순서대로 입력
# 출력 문장
# XX 행 열차가 들어오고 있습니다.

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1)
print(2-1)
print(5*2)
print(4/2)

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1 
print(5//3) # 몫 1

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(4 <= 4) # True

print(3 == 3) # True
print(4 == 2) # False

print(1 != 3) # True
print(not(1 != 3)) #False

# and 둘 다 만족해야 True
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

# or 하나만 만족해도 True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

# 간단한 수식
print(2 + 3 * 4) #14
number = 2 + 3  * 4
print(number)
number = number + 2 # 16
print(number)
number += 2
print(number) # 18
number *= 2 
print(number) # 36
number /= 2 
print(number) # 18
number -= 2
print(number) # 16

number %= 5 
print(number) # 1

# 절대값 abs
print(abs(-5)) # 5

# 제곱 pow
print(pow(4, 2)) # 4^2 = 16

# 최대값 max
print(max(5, 2)) # 5

# 최소값 min
print(min(5, 2)) # 2

# 반올림 round
print(round(3.14)) # 3
print(round(4.99)) # 5
