import enchant as en


wordlist = []
def file_to_list(file):
	err_f = open("error_log","w")
	error = 0
	non_english = 0
	d = en.Dict("en_US") 

	for line in file:
		try:
			newLine = line.strip('\n')
			if(newLine[-2:]=="'s"):
				newLine = newLine[0:len(newLine)-2]
			#remove non-english words
			if(len(newLine) > 0 and d.check(newLine)):
				wordlist.append(newLine.lower())
			else:
				non_english+=1
		except Exception as e:
			pos = "Some error : " + str(e)
			err_f.write(pos)		
			error = error + 1
	err_f.close()
	return wordlist, non_english