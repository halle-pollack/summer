import ast
from pprint import pprint
nGood = False
n2Good = False
same_len = False

word_list = open('enable1.txt').read().splitlines()

f = open('one_letter.txt').read()
possible_words_d=ast.literal_eval(f)


n = input("starting word:")
n2 = input("target word:")


while len(n) != len(n2) or not nGood or not n2Good:
	
	if n in word_list:
		nGood = True
	else:
			print(n + " is not in the dictionary!")
			n = input("starting word:")
	if n2 in word_list:
		n2Good = True
	else:
			print(n2 + " is not in the dictionary!")
			n2 = input("target word:")

	if len(n) == len(n2):
		same_len = True
	else:

		print("words must be the same length!")
		n = input("starting word:")
		n2 = input("target word:")
	


t1 = [[] for i in range(len(possible_words_d[len(n)][n]))]

ind = 0
for word in possible_words_d[len(n)][n]:
	t1[ind].append(word)
	ind +=1

