wordlist = []


x = input()
y = x.split('\t')

while(x!='*'):
	if(x==' ' or x=='\n'):
		x = input()
		y = x.split('\t')
		continue;

	if(y!=[' ']):
		wordlist.append(y)
	x = input()
	y = list(x.split('\t'))
	try:
		try:
			y[1] = list(y[1].split(' or '))
		except:
			a = 0
		#print(y[1])
	except:
		print("None")
	print(y)
