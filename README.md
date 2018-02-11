# Stemming
NLP Assignment 1

ABOUT
	The main program is main.py

	The input is read from a file (words.txt)
	Note : each word must be present on a separate line in the text file

	For removing english words, the package enchant has been used.
	It was installed using : pip install pyenchant


	It uses the following files :
		rules.py - contains stemming rules
		input_handler.py

	These files have been imported within main.py

	If the stemmed words are to be printed, uncomment line13 (print(wordList)) of main.py

	It creates a file named "error_log" in case of any exceptions with the position as which they occur
	Error such as "pos3 : string index out of range" is taken care of, and may be ignored. 

WHAT THE PROGRAM DOES
	The program is an effort to stem words by using grammar rules to remove as many plurals and suffixes as possible, correctly.
	The grammar rules used may be seen in rules.py

	The text file is parsed to a list of words after removing the non-english words
	This is done in input_handler.py

HOW TO RUN
	Run using : python3 main.py > output
	Note : preferably use redirection for the output to a file as the output may be very large

RESULT
	INPUT FILE
		words.txt

	OUTPUT 
		Number of words to be stemmed :  121966
		Words Scanned :  121966
		Non-english words removed :  344578
		ING words removed :  1195
		ISM words removed :  234
		other words removed :  28291

	UNDERSTANDING THE OUTPUT
		The number of words to be stemmed and Words Scanned is to ensure that each word present in the list has undergone processing. 
		If there are no errors, the two values will be equal
		If there are any errors, they will be logged in "error_log" file with the position in the program at which they have been caught.

		The number of non-english words removed is printed.

		The -ING ang -ISM and "other words" numbers tell how many such words were stemmed and found to be already present in the list.

		"ING words" implies words ending with -ing that were stemmed
		"ISM words" implies words ending with -ism that were stemmed
		"other words" implies words(nouns and verbs) with plurals and other miscellaneous suffixes(-ment,-ship) that were stemmed
		
