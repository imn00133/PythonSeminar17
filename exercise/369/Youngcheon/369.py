num = int(input("How long?\n"))
seed = int(input("seed: "))
linelen = int(input("Line length: "))
nodap = []
for i in range(1,num+1):
    nodap = list(str(i))
    repeat=0
    for j in nodap:
        if int(j)==0:
            pass
        else:
            if int(j)%seed==0:
                repeat += 1
    if repeat != 0:
        print("\""+"¦"*repeat+"\"", end=" ")
    else:
        print(i, end=" ")
    if int(i) % linelen == 0:
            print("")

