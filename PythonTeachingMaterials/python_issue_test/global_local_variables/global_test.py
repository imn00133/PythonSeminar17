def a():
    global a
    a += 1
    print(a)
    print("local 확인")
    print(locals())


a = 1
print("global 사용 전")
print(globals())
a()
print("global 사용 후")
print(globals())
a()
print(a)
