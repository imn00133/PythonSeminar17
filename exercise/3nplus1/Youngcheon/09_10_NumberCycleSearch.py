def Cycle(Num):
    i = 1
    while Num != 1:
        if Num%2 == 0:
            Num /= 2
            i += 1
        else:
            Num = Num*3+1
            i += 1
    return int(i)

while 1:
    Start = int(input("Start : "))
    End = int(input("End : "))
    Longest = Cycle(Start)
    for i in range(Start+1, End+1):
        if Longest < Cycle(i):
            Longest = Cycle(i)
    print(Longest)
