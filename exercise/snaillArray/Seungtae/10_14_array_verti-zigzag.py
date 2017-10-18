matrix=[[0 for col in range(100)] for row in range(100)]
Matrix=[[0 for col in range(100)] for row in range(100)]

mcol=int(input("행의 개수는: "))
nrow=int(input("열의 개수는: "))

i=0
j=0
num=1
for i in range(nrow):
	if i%2==0:
		for j in range(mcol):
			matrix[i][j]=num
			num+=1
	else:
		for j in range(mcol-1,-1,-1):
			matrix[i][j]=num
			num+=1
	i+=1
	
for i in range(nrow):
	for j in range(mcol):
		Matrix[j][i]=matrix[i][j]
	
for i in range(mcol):
	for j in range(nrow):
		print(Matrix[i][j], end=" ")
	print("")