import string
from pprint import pprint

global az
global letter_num

az = string.ascii_lowercase

letter_num = {}

count = 1
for letter in az:
	letter_num[letter] = count
	count +=1

def alpha_cycle(start):

	c = az[letter_num[start]-1:] + az[:letter_num[start]-1]
	#print(c)
	return c


def get_letter(alpha_c,letter):
	d = alpha_c[letter_num[letter]-1]
	#print(d)
	return d

def translate(secret, message):

	lens=len(secret)
	lenm=len(message)

	n=int(lenm/lens)+1
	lsw=secret*n
	secret = lsw[:lenm]
	full = []
	for i in range(len(message)):
		full.append(get_letter(alpha_cycle(secret[i]),message[i]))
	print('\n')
	print(''.join(full))
	return 0




secret=input("what is the secret word? " )
message=input('what is the message? ')
message=(''.join(ch for ch in message if ch.isalnum()))

translate(secret,message)