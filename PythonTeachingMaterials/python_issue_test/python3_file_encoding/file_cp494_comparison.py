# cp494로 되어있는 문자열을 읽어왔을 때, utf-8과 비교 문제가 발생하는지 확인해보았다.
# 불러들인 문자열은 utf-8로 바뀌는게 아닌가 싶다.

f = open("encoding_test.txt", "r")
line = f.readline()
print(line == "1번째 줄입니다.\n")
print(line.count('1'))
f.close()