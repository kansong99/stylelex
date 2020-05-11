import spacy

nlp = spacy.load("en_core_web_sm")

text = ("Kofi has bought 123,564 grapes")


bigNums = ['hundred', 'thousand', 'million', 'billion', 'trillion']

def wholeGreaterThan(ent): # A function to determine if a number is greater than one hundred and ends with 00s
	for num in bigNums:
		if num in ent and ent[len(ent) - len(num):] is num:
			if num is 'hundred' and (ent[:4] is 'one' or ent[:4] is 'One'):
				return False
			return True
	return False

def greaterThan(ent):
	for num in bigNums:
		if num in ent.text:
			return True
	return False


def hasSign(text, start_char): #function to tell if dollar or $ is used
	if text[start_char - 1] is '$' or text[start_char - 2] is '$':
		return True
	return False



doc = nlp(text)

for ent in doc.ents:
	first = text[ent.start_char]
	last = text[ent.end_char - 1]
	word = ent.text
	if ent.label_ is 'CARDINAL' or ent.label_ is 'MONEY' or ent.label_ is 'QUANTITY' or ent.label_ is 'DATE':
		startCheck = ent.start_char #check if we are starting a sentence.
		ending = text[ent.end_char - 1 :ent.end_char + 1] #check to validate last two chars are not 00
		if ((startCheck > 3) and (text[startCheck - 2: startCheck] is '. ' or text[startCheck - 3: startCheck] is '.  ')) or startCheck is 0: #starts sentence
			if first.isnumeric() and ent.label_ is not 'DATE':
				print("spell out numbers when they start sentence")
			elif first.isnumeric() and ent.label_ is 'DATE':
				print("Consider rephrasing sentence so it does not start with date")

		elif ent.label_ is 'MONEY': #Applying the rules for money
			if "dollars" in ent.text: #I had to account for this due to negligence, effectively removing dollars
				if ent.text[len(ent.text) - 8] == ' ':
					last = ent.text[len(ent.text) - 9]
					word = ent.text[:len(ent.text) - 8]
				else:
					last = ent.text[len(ent.text) - (8)]
					word = ent.text[:len(ent.text) - 7]
			if first.isnumeric() and last.isnumeric(): #this means word is a number, should be greater than 100 or decimal
				if (int(word) >= 100 and ending is not '00') or '.' in ent.text: #This is good and means we should use $
					if hasSign(text, start) is False:
						print("You should use $ when money is numeral")
				elif ending is '00':
					if hasSign(text, startCheck): #if ending indicates text should be written and they used $
						print("Write out round numbers and use dollars instead of $")
					else: #they did not use $ but did not spell out round number
						print("Write out round numbers e.g, twenty-seven thousand")
				elif int(word) < 100:
					if hasSign(text, startCheck):
						print("spell out numbers less than 100 and use dollars instead of $")
					else:
						print("spell out numbers less than 100")
			elif first.isnumeric(): #they used number to start then spellled out rest, 27 hundred
				print("Spell out numbers greater than hundred and use dollars")
			else: #two letters, negleting scenario where alpha starts and numeric ends, as unlikely
				if wholeGreaterThan(word) and hasSign(text, startCheck): #This means they spell out word but don't use dollars
					print("use dollars for numbers greater than 100")
				if greaterThan(ent): #test to see if they are spelling out big number
					if hasSign(text, startCheck):
						print("don't spell out number greater than 100")
					else:
						print("don't spell out number greater than 100 and use $ instead of dollars")
				if hasSign(text, startCheck):
					print("dollars should be used instead of $ for numbers less than or equal to 100")






