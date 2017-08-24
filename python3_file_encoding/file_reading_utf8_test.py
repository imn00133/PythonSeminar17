import sys

print(sys.getdefaultencoding())
print(sys.stdin.encoding)
print(sys.stdout.encoding)

f = open("encoding_test_utf8.txt", "r", encoding="utf-8")

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
