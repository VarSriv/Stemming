import rules as rule
import input_handler as ip

file = open("words.txt")
# file = open("my.txt")

wordlist,non_english = ip.file_to_list(file)

print("Number of words to be stemmed : ",len(wordlist))

try:
	wordlist,dupl_other,dupl_ing,dupl_ism = rule.stem(wordlist)
	#print(wordlist)
	print("Non-english words removed : ",non_english)
	print("ING words removed : ",dupl_ing)
	print("ISM words removed : ",dupl_ism)
	print("other words removed : ",dupl_other)
except Exception as e:
	print("Something went wrong : ",e)