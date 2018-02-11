def isVowel(ch):
	if(ch in ['a','e','i','o','u']):
		return True

def plural_rules(word):

	#headmistresses, roses, echoes
	if(word[-4:] == "sses"  or word in ["echoes"]):
		word = word[0:len(word)-2]

	if(word in ["toes","ices"] or word[-4:] == "oses"):
		word = (word[0:len(word)-1])

	#ses -> sis
	if(word[-3:]=='ses'):
		if(word in ["abacuses"]):
			word = (word[0:len(word)-2])
		else:
			word = (word[0:len(word)-2]+'is')

	#ves -> f
	#ives -> fe
	if(word[-3:]=='ves'):
		if(word[-4]=='i'):
			word = (word[0:len(word)-3]+'fe')
		else:
			word = (word[0:len(word)-3]+'f')
	if(word[-3:]=="ies"):
		word = (word[0:len(word)-3]+'y')

	if(word[-4:]=="ices"):
		#exception
		if(word in ["matrices","apendices"]):
			word = (word[0:len(word)-4]+"ix")
		else:
			word = (word[0:len(word)-4]+"ex")

	#for plurals ending in ia  #ia->ium		
	if(word[-2:]=="ia"):
		#exceptions
		if(word in ["hysteria","cafeteria"]):
			word = (word)
		#bacteria, media
		else:
			word = (word[0:len(word)-1]+"um")

	#men -> man		
	if(word[-3:]=="men"):
		word = (word[0:len(word)-3]+"man")

	if(word in ["mice","lice"]):
		word = (word[0:len(word)-3]+"ouse")

	if(word == "children"):
		word = ("child");

	#algae = alga
	if(word[-2:] == "ae"):
		word = (word[0:len(word)-1])

	if(not isVowel(word[-2]) and word[-1]=='s'):
		word = (word[0:len(word)-1])

	return word


def rules3(word):

	if(word[-3:] in ["tes","des","kes","ted","nes","ces","rer","zed","zes","ued"]):
		word = word[0:len(word)-1]
		if(word[-3:] in ["cte","lte","rte"]):
			word = word[0:len(word)-1]

	if(word[-3:] in ["ned","hes","hed","tal"]):
		word = word[0:len(word)-2]

	if(word[-4:] in ["tion","tive"]):
		word = word[0:len(word)-3]+"e"
		if(word[-3:] in ["cte","rte","lte"]):
			word = word[0:len(word)-1]

	if(word[-4:] in ["nder","nded"]):
		word = word[0:len(word)-2]

	return word

def rules2(word):

	if(word[-5:] in ["nment","hment","ement"]):
		word = (word[0:len(word)-4])

	if(word[-5:] in ["iment"]):
		word = (word[0:len(word)-5]+"y")
		
	if(word[-2:] == "ly"):
		#print("yea")
		if(word[-3]=="b"):
			word = word[0:len(word)-1]+"e"
		else:
			word = (word[0:len(word)-2])

	return word


def stem(wordlist):
	error = 0
	dupl_ing = 0
	dupl_lte3 = 0
	dupl_other = 0
	dupl_ism = 0
	word_scanned = 0
	stemmedList = []

	err_f = open("error_log","a")
	err_f.write("Error logs\n")

	for word in wordlist:

		word_scanned+=1

		#words too short to not be in root form
		if(len(word)<=3):
			dupl_lte3 += 1
			if(word not in stemmedList):
				stemmedList.append(word)
			continue
		
		#list of words(exceptions) not following the "plural" rules
		exceptions = ["iris","moses","goddess","ship","after","across"]
		if(word in exceptions):
			#print(word)
			stemmedList.append(word)
			continue #go to the next word
		#------------------------------------------------
		try:
			if(word[-4:] in ["ness","ship"]):
				if(word[-5]=='i'):
					word = (word[0:len(word)-5]+"y")
				else: 
					word = (word[0:len(word)-4])
		#pos1
		except Exception as e:
			pos1 = "pos1 : " + str(e)
			err_f.write(pos1);
			error +=1
		#------------------------------------------------
		try:
			word = plural_rules(word)
		except Exception as e:
			pos2 = "pos2 : " + str(e) + "\n"
			err_f.write(pos2);
			error = error + 1
		#print("Changed : ",word)
		#------------------------------------------------
		try:
			word = rules2(word)
		except Exception as e:
			pos3 = "pos3 : " + str(e) +"\n"
			err_f.write(pos3);
			error += 1
		#------------------------------------------------
		try:
			word = rules3(word)
		except Exception as e:
			pos4 = "pos4 : " + str(e) + "\n"
			err_f.write(pos4);
			error += 1
		#print("After some more changes : ",word)
		#------------------------------------------------

		#remove -ing 
		#--> stemming = stem bathing = bathe cooling = cool
		try:
			if(word[-3:] == "ing"):
				#thing,sing
				if(len(word)-3 < 3):
					#print(word)
					if(word not in stemmedList):
						stemmedList.append(word)
					continue

				flag = 0
				word = word[0:len(word)-3] #remove -ing
				#making, baking = make,bake #loving=love #caring=care
				if(not flag):
					if(word[-2:] in ['ar','ov','ak']):
						word = (word+"e")
						if(word in stemmedList):
							dupl_ing+=1
						else:
							stemmedList.append(word)
						flag = 1

				#cooling, fooling

				if(not flag):
					if(word[-3:] in ['ank','ack','ink','ill'] or "oo" in word ):
						if(word in stemmedList):
							dupl_ing+=1
						else:
							stemmedList.append(word)
						flag = 1
						

				#stemming, fulfilling = stem, fulfil

				if(not flag and word[-1] == word[-2]):
					word = (word[0:len(word)-1])
					if(word in stemmedList):
						dupl_ing+=1
					else:
						stemmedList.append(word)
			#---------------------------------------------------------------------
			elif(len(word)>5 and word[-3:] == "ism"):
				if(word in ["anabolism","anachronism","altruism"]):
					word = word
				elif(word[-4] in ['e','c','n','r','l']):
					word = word[0:len(word)-3]
				elif(word[-4] in ['t','v','r']):
					word = word[0:len(word)-3]+'e'
				elif(word[-4]=='h' and word[-5]=='c'):
					word = word[0:len(word)-3]+'y'
				if(word in stemmedList):
						dupl_ism+=1
				else:
					stemmedList.append(word)
			#---------------------------------------------------------------------
			else:
				#print(word)
				if(word in stemmedList):
					dupl_other+=1
				else:
					stemmedList.append(word)

		except Exception as e:
			pos = "pos5 : " + str(e) + "\n"
			err_f.write(pos);
			#stemmedList.append(word)
			error += 1

	#end of for loop
	err_f.close()
	print("Words Scanned : ",word_scanned)

	return stemmedList,dupl_other,dupl_ing,dupl_ism
