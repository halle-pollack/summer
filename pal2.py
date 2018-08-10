n = open('pal_input.txt').read().splitlines()
n = "\n".join(n)

print('-------------------')
print(n)
print('-------------------')







n=n.lower()

newN = []

for item in list(n):
	if item.isalpha():
		newN.append(item)

orig_n=''.join(newN)
rev_n = orig_n[::-1]

if orig_n == rev_n:
	print("Palindrome")
else:
	print("Not a Palindrome")