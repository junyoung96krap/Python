score_file = open("score.txt", "w", encoding="utf8") # "w" 쓰기 용도
print("수학 : 0", file=score_file)
print("영어 : 100", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # "a" 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # "r" 파일에 있는 내용 읽어오기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()