# 일반적인 open으로 write하였다.
# 결과값은 cp494로 저장된다.

f = open("encoding_test.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
