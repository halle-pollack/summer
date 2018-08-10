from pprint import pprint

import itertools

q = input("enter integers followed by a target: ")
q=[int(i) for i in q.split(" ")]
target_ans=q[-1:][0]


q_perm = list(itertools.permutations(q[:-1]))
#pprint(q_perm)

op_perm=list(itertools.product(['+','-','*','/'],repeat = len(q)-2))
#pprint(op_perm)





def left_solve(prob):

	
	new_prob = []

	for x in range(len(prob)//2):
		l="".join(prob[0:3])
		ans = eval(l)

		prob[2]= str(ans)
		prob = prob[2:]
		#print(prob)

	if float(prob[0]).is_integer():
		#print(int(float(prob[0])))
		return int(float(prob[0]))
	else:
		#print('not valid')
		return -1
	
	




def make_prob(num_tup, op_tup):
	prob_list = [str(num_tup[0])]
	ind = 0
	for num in num_tup[1:]:
		prob_list.append(op_tup[ind])
		prob_list.append(str(num))
		ind+=1


	return prob_list

def print_prob(num_tup, op_tup, target_ans):
	prob_list = make_prob(num_tup,op_tup)
	prob_string = ' '.join(prob_list)
	print(prob_string + ' = ' + str(target_ans))
	return -1


for p in q_perm:
	for op in op_perm:

	
		ans = left_solve(make_prob(p,op))
		if ans == target_ans:
			print_prob(p,op,target_ans)
			print("\n")

