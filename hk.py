import requests
from pprint import pprint
from random import randint
print("\n")
n=input("What topic would you like your haiku to be about? ")

url1 = "https://api.datamuse.com/words?rel_jjb="+ n + "&md=s&max=500"
r1 = requests.get(url1)
url2 = "https://api.datamuse.com/words?rel_jja="+ n + "&md=s&max=500"
r2 = requests.get(url2)

data1 = r1.json()
data2 = r2.json()
data = data1+data2


def  pickWord():

	ind = randint(0,len(data)-1)
	word_info = data[ind]
	del data[ind]
	num_syl = word_info["numSyllables"]
	new_word =word_info["word"]
	#print(num_syl)
	#print(new_word)
	word_info = {"new_word":new_word, "num_syl": num_syl}

	return word_info;


def makeLine(num_of_syls):

	new_line = []
	total_syl = 0

	while total_syl < num_of_syls:
		word_info = pickWord()
		syl=int(word_info["num_syl"])
		while (syl > (num_of_syls-total_syl)):
			word_info = pickWord()
			syl=int(word_info["num_syl"])

		total_syl += syl
		new_line.append(word_info["new_word"])
	printed_line=" ".join(new_line)
	print("\t" + printed_line)
	return -1;

print("\n\tYour haiku is titled '" + n.capitalize() + "'\n")

makeLine(5) 

makeLine(7) 

makeLine(5) 


