import spacy
from links import *

bigNums = ['hundred', 'thousand', 'million', 'billion', 'trillion']

def wholeGreaterThan(ent): # A function to determine if a number is greater than one hundred and ends with 00s
	for num in bigNums:
		if (num in ent) and (ent[len(ent) - len(num):] == num):
			if num == 'hundred' and ent[:4] in {'one', 'One'}:
				return False
			return True
	return False

def greaterThan(ent):
	for num in bigNums:
		if num in ent.text:
			return True
	return False


def hasSign(text, start_char): #function to tell if dollar or $ is used
	if text[start_char - 1] == '$' or text[start_char - 2] == '$' or text[start_char] == '$':
		return True
	return False

def quantage(tag, word, start, end, quant0, quant1): # function to handle degrees or percentages
	if tag != 'PERCENT':
		bool1 = word[0].isnumeric() == True
		binary(bool1, 4, 6, quant0, start, end)
	if tag == 'PERCENT':
		if '%' in word:
			bool1 = True
		else:
			bool1 = False
		binary(bool1, 8, 10, quant1, start, end)

def numb_func(quant0, quant1, quant3, quant4, quant5, quant6):
	#first boolean determines whether you want to express degrees or measurements as symbols (0) or written out (1)
	#second boolean determines whether you want to write out percent (1) or use the symbol (0)
	#third boolean checks whether you want to perform checks on date formatting
	#fourth boolean checks if you want to write age as numeral
	#fifth boolean checks if you want to write out decades
	#sixth boolean checks if you want numbers and money <= 100 to be symbols and > 100 witten out
	for ent in doc.ents:
		first = text[ent.start_char]
		last = text[ent.end_char - 1]
		word = ent.text
		if word[0] == '$': #make it so that $ does not mess with things
			word = word[1:]
			first = word[0]
		if ent.label_ == 'CARDINAL' or ent.label_ == 'MONEY' or ent.label_ is 'QUANTITY' or ent.label_ is 'DATE' or ent.label_ is 'PERCENT':
			startCheck = ent.start_char #check if we are starting a sentence.
			ending = text[-2:] #check to validate last two chars are not 00
			if quant3 and (((startCheck > 3) and (text[startCheck - 2: startCheck] == '. ' or text[startCheck - 3: startCheck] == '.  ')) or startCheck == 0): #starts sentence
				if first.isnumeric() and ent.label_ is not 'DATE':
					llist.insert(startCheck, 12)
				elif first.isnumeric() and ent.label_ is 'DATE':
					llist.insert(startCheck, 14)
			elif quant4 and (ent.label_ is 'DATE' and ('year' in word and 'old' in word)): #the assumption being this is an age
				if text[ent.start_char].isnumeric() is False:
					llist.insert(startCheck, 16)
			elif quant5 and ent.label_ is 'DATE' and (word[0] in {"\'", "1", "2"} and word[-1] == "s"): #this suggests we are working with decade
				llist.insert(startCheck, 18)
			elif quant6 and ent.label_ in {'MONEY', 'CARDINAL'}: #Applying the rules for money
				if "dollars" in ent.text: #I had to account for this due to negligence, effectively removing dollars
					if ent.text[len(ent.text) - 8] == ' ':
						last = ent.text[len(ent.text) - 9]
						word = ent.text[:len(ent.text) - 8]
						ending = word[len(word) - 2:]
					else:
						last = ent.text[len(ent.text) - (8)]
						word = ent.text[:len(ent.text) - 7]
						ending = word[len(word) - 2:]
				if first.isnumeric() and last.isnumeric(): #this means word is a number, should be greater than 100 or decimal
					if word == '100':
						llist.insert(startCheck, 20)
					elif ',' in word and len(word) > 3 or '.' in word or (int(word) >= 100 and ending != '00'): #This is good and means we should use $
						if ent.label_ == 'MONEY' and hasSign(text, startCheck) is False:
							llist.insert(startCheck, 22)
					elif ending == '00':
						if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
							llist.insert(startCheck, 24)
						else: #they did not use $ but did not spell out round number
							llist.insert(startCheck, 26)
					elif int(word) < 100:
						if ent.label_ == 'MONEY' and hasSign(text, startCheck):
							llist.insert(startCheck, 28)
						else:
							llist.insert(ent.start_char, 2)
				elif first.isnumeric(): #they used number to start then spellled out rest, 27 hundred
					if word[-2:] not in {'on', 'nd', 'ed'}: #number ends in thousand, million, hundred, etc... 
						if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
							llist.insert(startCheck, 30)
						else: #they did not use $ but did not spell out round number
							llist.insert(startCheck, 32)
					else:
						if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
							llist.insert(startCheck, 34)
						else: #they did not use $ but did not spell out round number
							llist.insert(startCheck, 36)
				#it seems spacy will not register these situations as MONEY but as cardinal			
				else: #two letters, negleting scenario where alpha starts and numeric ends, as unlikely
					if wholeGreaterThan(word):
						if ent.label_ == 'MONEY' and hasSign(text, startCheck): #This means they spell out word but don't use dollars
							llist.insert(startCheck, 38)
					elif greaterThan(ent): #test to see if they are spelling out big number
						if ent.label_ == 'MONEY' and hasSign(text, startCheck):
							llist.insert(startCheck, 40)
						else:
							llist.insert(startCheck, 42)
					elif ent.label_ == 'MONEY' and hasSign(text, startCheck):
						llist.insert(startCheck, 44)
			elif ent.label_ in {'QUANTITY', 'PERCENT'}: #then you want it to be numerals and not spelled out
				quantage(ent.label_, ent.text, ent.start_char, ent.end_char, quant0, quant1)





