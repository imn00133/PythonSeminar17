user_number=int(input("숫자를 입력하세요: "))
number_of_clap=0
for i in range(1,user_number+1):
	if i%10==3 or i%10==6 or i%10==9:
		number_of_clap=number_of_clap+1
		if i%100-i%10==30 or i%100-i%10==60 or i%100-i%10==90:
			number_of_clap=number_of_clap+1
			if i%1000-i%100==300 or i%1000-i%100==600 or i%1000-i%100==900:
				number_of_clap=number_of_clap+1
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
			else :
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
		else :
			if i%1000-i%100==300 or i%1000-i%100==600 or i%1000-i%100==900:
				number_of_clap=number_of_clap+1
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
			else :
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
	else :
		if i%100-i%10==30 or i%100-i%10==60 or i%100-i%10==90:
			number_of_clap=number_of_clap+1
			if i%1000-i%100==300 or i%1000-i%100==600 or i%1000-i%100==900:
				number_of_clap=number_of_clap+1
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
			else :
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
		else :
			if i%1000-i%100==300 or i%1000-i%100==600 or i%1000-i%100==900:
				number_of_clap=number_of_clap+1
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
			else :
				if i%10000-i%1000==3000 or i%10000-i%1000==6000 or i%10000-i%1000==9000:
					number_of_clap=number_of_clap+1
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
				else :
					if i%100000-i%10000==30000 or i%100000-i%10000==60000 or i%100000-i%10000==90000:
						number_of_clap=number_of_clap+1
	if number_of_clap>=1:	
		print("짝"*number_of_clap, end=" ")
		number_of_clap=0
	else :
		print(i, end=" ")
	if i%20==0:
		print(" ")
	
