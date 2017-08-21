linev=int(input("행을 입력하시오: "))
lineh=int(input("열을 입력하시오: "))
verticle_line=[]
horizontal_line=[]
for i in range(0,linev):
	for j in range(1,lineh+1):
		horizontal_line=horizontal_line+[j]
	verticle_line=verticle_line+[horizontal_line]
for a in range(0,linev):
	for b in range(0,lineh):
		verticle_line[a][b]=verticle_line[a][b]+lineh*a
		print(verticle_line[a][b], end=" ")
		if b==lineh-1:
			print(" ")
			
	
