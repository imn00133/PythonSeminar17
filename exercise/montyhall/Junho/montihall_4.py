import random
i=0
sum=0
while(i<100000):
    gift=["Car","lamb","Goat","dog"]
    choice=random.randint(0,3)
    if choice==0:
        del gift[random.randint(1,3)]
        choice=random.randint(1,2)
    elif choice==1:
        del gift[random.randint(2,3)]
        choice=0 or choice=2
    elif choice==2:
        del (gift[1]) or del (gift[3])
        choice=0 or choice=2
    else:
        del gift[random.randint(1,2)]
        choice=random.randint(0.2)
    if choice==0:
        sum+=1
        print("차 가져가")
    else:
        print("집 걸어가")
    i+=1
    print(sum/i)