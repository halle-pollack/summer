n = 5
x = 1
grid_order =[]

grid = [[0 for i in range(n)] for j in range(n)]


space = len(str(grid))

#for i in range(0, n):
	#for j in range(0,n):
		#grid[i][j] = x
	#	x +=1
		
	#	grid_order.append([i,j])



# 1  2  3  4 5
#16 17 18 19 6
#15 24 25 20 7
#14 23 22 21 8
#13 12 11 10 9


def make_i(n):

	r = []

	for x in range(n): # 0 0 0 0 0
		r.append(0)

	for x in range(1,n): # 1 2 3 4
		r.append(x)

	for x in range(n-1): # 4 4 4 4
		r.append(n-1)

	for x in range(n-2,0,-1): #3 2 1
		r.append(x)

	for x in range(n-2): # 1 1 1
		r.append(1)
	for x in range(2,n-1): #2 3
		r.append(x)
	for x in range(n-3): # 3 3
		r.append(n-2)
	for x in range(n-3):
		r.append(n-3)

	return r

i = [0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 1, 1, 1, 2, 3, 3, 3, 2, 2]
j = [0, 1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 3, 2, 1, 1, 2]



for pair in range(0,n*n):
		grid[i[pair]][j[pair]]= x
		x +=1

for line in grid:
	print(line)



