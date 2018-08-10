from pprint import pprint
import string
word_list = open('enable1.txt').read().splitlines()

rev_word_list = []
possible_words = []
new = []
first2 = []
count = 0
max_word = ''
max_word_len = 0



for word in word_list:
	rev_word_list.append(word[::-1])
	first2.append(word[0:2])



first2=set(first2)

first2_dict = {k: [] for k in first2}
rev_dict = dict(zip(word_list,rev_word_list))



for x in first2:
#	print('-----------------------------------------------')
	#print(x)
	#print('-----------------------------------------------')
	for word in word_list:
		if x == word[::-1][0:2]:
			first2_dict[x].append(word)
			#print(word)

#print("finished")







def pal(word1,word2):
	total = word1 + word2
	total_back = total[::-1]
	if total == total_back:
		print(word1 +" " + word2)

		return (True,str((word1 +" " + word2)))
	else:
		return (False,'') 


def make_possible_list(word,word_list,rev_dict):
	poss_list = []
	for x in word_list:
		if word[0:2] == rev_dict[x][0:2]:
			poss_list.append(x)
	return poss_list




for word1 in word_list:
	word_list2 = first2_dict[word1[0:2]]
	for word2 in word_list2:
		if word1 != word2:
			exist, total_word= pal(word1,word2)
			if(exist):
				count+=1
				#if len(total_word) >= max_word_len:
					#max_word_len = len(total_word)
					#max_word = total_word
					#print(max_word)
print(count)