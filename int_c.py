
A = int(input("enter a number:"))
current = A+1
factor = []
total_sum = []
num_range = list(range(1,int(A/2)+1))

for x in num_range:
	if A%x==0:
		y = A//x
		#print("factor found! " + str(x) + " and " + str(y))
		
		factor.append(x)
		factor.append(y)
		total = x + y
		total_sum.append(total)


		if x + y <= current:
			best1,best2 = x,y
			current = x + y

		if y < A/2:
			num_range.remove(y)



	#print(x)
factor=list(set(factor))
factor.sort()
print(factor)
#print(total_sum)
#print(current)
print(str(best1) + "*" + str(best2) + "=" + str(A))
print(str(best1) + "+" + str(best2) + "="  + str(current))