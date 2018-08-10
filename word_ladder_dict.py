from pprint import pprint
import string
word_list = open('enable1.txt').read().splitlines()

len_list = []
for word in word_list:
	len_list.append(len(word))

len_list=set(len_list)
word_len_dict={k: [] for k in len_list}

for word in word_list:
	word_len_dict[len(word)].append(word)


one_diff = False
count = 0





def comp_word(word1,word2):
	count = 0
	if len(word1) != len(word2):
		print("words aren't the same length")
		return False

	for x in range(len(word1)):
		if word1[x] != word2[x]:
			count +=1
	if count ==1:
		return True
	else:
		return False



one_letter={k: [] for k in word_len_dict}

for i in len_list:
	one_letter[i]={k: [] for k in word_len_dict[i]}


for i in len_list:
	for word1 in word_len_dict[i]:
		for word2 in word_len_dict[i]:
			if comp_word(word1,word2):
				one_letter[i][word1].append(word2)
		print(word1)
		print(one_letter[i][word1])