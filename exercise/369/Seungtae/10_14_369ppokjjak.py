def PPokJJak(number):
	i=0
	jjak=0
	num=str(number)
	arr=[]
	while i<len(num):
		if num[i]=='0':
			pass
		elif int(num[i])%6==0:
			arr.append("뽁짝")
		elif int(num[i])%2==0:
			arr.append("뽁")
		elif int(num[i])%3==0:
			arr.append("짝")
		else:
			pass
		i+=1			
	return arr

n=int(input("우리의 삼육구 게임이 어디까지 갈까?: "))
num=1
while num<=n:
	arr=PPokJJak(num)
	if not(arr):
		print("%d" %num,end=" ")
	else:
		for p in range(0,len(arr)):
			print(arr[p],end="")
		print(end=" ")
	if num%10==0 and num>1:
		print("")
	num+=1