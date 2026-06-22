cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

print(3 in cabinet)
print(5 in cabinet)

# 새 손님
print(cabinet)
cabinet[3] = "김종국"
cabinet[5] = "박명수"
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 폐점
cabinet.clear()
print(cabinet)