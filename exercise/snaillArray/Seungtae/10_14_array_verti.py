matrix=[[0 for col in range(100)] for row in range(100)]

nrow=int(input("행의 개수는: "))
mcol=int(input("열의 개수는: "))

i=0
j=0
num=1

while j<mcol:
	for i in range(0,nrow):
		matrix[i][j]=num
		num+=1
	j+=1
	
for i in range(nrow):
	for j in range(mcol):
		print(matrix[i][j], end=" ")
	print("")