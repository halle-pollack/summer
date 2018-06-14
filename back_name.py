name = raw_input("type in your name: ")

l = name[::-1].split()
l.reverse()
print(' '.join(l))
