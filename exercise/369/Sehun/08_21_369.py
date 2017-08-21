while True:
	number = int(input("숫자를 입력하세요 : "))
	if number >=1 and number <=10000:
		for a in range(1,(number+1)):
			if a == number and a%10 in [3, 6, 9]:
				print("짝!")
			elif a == number:
				print(a)
			elif a%10 in [3, 6, 9]:
				print("짝!", end=" ")
			elif a%20 == 0:
				print(a)
			else:
				print(a, end=" ")
	else:
		print("1이상 10000이하의 숫자만 입력할 수 있습니다.")