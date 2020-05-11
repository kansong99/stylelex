import spacy

nlp = spacy.load("en_core_web_sm")

text = ("1927 was when blacks became new slaves")

bigNums = ['hundred', 'thousand', 'million', 'billion', 'trillion']

def wholeGreaterThan(ent): # A function to determine if a number is greater than one hundred and ends with 00s
	for num in bigNums:
		if num in ent.text and ent.text[len(ent.text) - len(num):] is num:
			if num is 'hundred' and (ent.text[:4] is 'one' or ent.text[:4] is 'One'):
				return False
			return True
	return False

def greaterThan(ent):
	for num in bigNums:
		if num in ent.text:
			return True
	return False


def hasSign(text, start_char): #function to tell if dollar or $ is used
	if text[ent.start_char - 1] is not '$' or text[ent.start_char - 2] is not '$':
		return False
	return True



doc = nlp(text)

for ent in doc.ents:
	if ent is 'CARDINAL' or ent is 'MONEY' or ent is 'QUANTITY':
		startCheck = ent.start_char #check if we are starting a sentence.
		ending = text[ent.end_char - 1 :ent.end_char + 1] #check to validate last two chars are not 00
		if (startCheck > 3) and (text[startCheck - 2: startCheck] is '. ' or text[startCheck - 3: startCheck] is '.  '): #starts sentence
			if ent.start_char.isnumeric() and ent.label_ is not 'DATE':
				print("spell out numbers when they start sentence")
			elif ent.start_char.isnumeric() and ent.label_ is 'DATE':
				print("Consider rephrasing sentence so it does not start with date")

		elif ent.label_ is 'MONEY': #Applying the rules for money
			if ent.start_char.isnumeric() and ent.end_char.isnumeric(): #this means word is a number, should be greater than 100 or decimal
				if (int(ent.text) >= 100 and ending is not '00') or '.' in ent.text: #This is good and means we should use $
					if hasSign(text, start) is False:
						print("You should use $ when money is numeral")
				elif ending is '00':
					print("Write out round numbers and use dollars instead of $")
				elif int(ent.text) < 100:
					print("spell out numbers less than 100 and use dollars instead of $")
			elif ent.start_char.numeric(): #they used number to start then spellled out rest, 27 hundred
				print("Spell out number and use dollars")
			else: #two letters, negleting scenario where alpha starts and numeric ends, as unlikely
				if wholeGreaterThan(ent) and hasSign(text, start_char): #This means they spell out word but don't use dollars
					print("use dollars for numbers greater than 100")
				if greaterThan(ent): #test to see if they are spelling out big number
					if hasSign(text, start_char):
						print("don't spell out number greater than 100")
					else:
						print("don't spell out number greater than 100 and use $ instead of dollars")
				if hasSign(text, start_char):
					print("dollars should be used instead of $ for numbers less than or equal to 100")













	print(ent.text, ent.start_char, ent.end_char, ent.label_)