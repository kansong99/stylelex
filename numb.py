import spacy

nlp = spacy.load("en_core_web_md")

text = ("Sam is celebrating his twenty-fourth birthday.")


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

def quantage(tag, word, start, end): # function to handle degrees or percentages
	if word[0].isnumeric() is False:
		print("Consider using numerals")
	if tag == 'PERCENT':
		if '%' in word:
			print("use percent and not %")




doc = nlp(text)
for ent in doc.ents:
	first = text[ent.start_char]
	last = text[ent.end_char - 1]
	word = ent.text
	if word[0] == '$': #make it so that $ does not mess with things
		word = word[1:]
		first = word[0]
	if ent.label_ is 'CARDINAL' or ent.label_ is 'MONEY' or ent.label_ is 'QUANTITY' or ent.label_ is 'DATE' or ent.label_ is 'PERCENT':
		startCheck = ent.start_char #check if we are starting a sentence.
		ending = text[-2:] #check to validate last two chars are not 00
		if ((startCheck > 3) and (text[startCheck - 2: startCheck] is '. ' or text[startCheck - 3: startCheck] is '.  ')) or startCheck is 0: #starts sentence
			if first.isnumeric() and ent.label_ is not 'DATE':
				print("spell out numbers when they start sentence")
			elif first.isnumeric() and ent.label_ is 'DATE':
				print("Consider rephrasing sentence so it does not start with date")

		elif ent.label_ is 'DATE' and ('year' in word and 'old' in word): #the assumption being this is an age
			if text[ent.start_char].isnumeric() is False:
				print("write age as numeral")
		elif ent.label_ is 'DATE' and (word[0] in {"\'", "1", "2"} and word[-1] == "s"): #this suggests we are working with decade
			print("spell out decades, e.g nineteen-sixties not '60s") 
		elif ent.label_ in {'MONEY', 'CARDINAL'}: #Applying the rules for money
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
					print("spell out words less than or equal to 100")
				elif ',' in word and len(word) > 3 or '.' in word or (int(word) >= 100 and ending != '00'): #This is good and means we should use $
					if ent.label_ == 'MONEY' and hasSign(text, startCheck) is False:
						print("You should use $ when money is numeral")
				elif ending == '00':
					if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
						print("Write out round numbers and use dollars instead of $")
					else: #they did not use $ but did not spell out round number
						print("Write out round numbers e.g, twenty-seven thousand dollars")
				elif int(word) < 100:
					if ent.label_ == 'MONEY' and hasSign(text, startCheck):
						print("spell out numbers less than 100 and use dollars instead of $")
					else:
						print("spell out numbers less than or equal to 100")
			elif first.isnumeric(): #they used number to start then spellled out rest, 27 hundred
				if word[-2:] not in {'on', 'nd', 'ed'}: #number ends in thousand, million, hundred, etc... 
					if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
						print("Write out whole number and use dollars instead of $")
					else: #they did not use $ but did not spell out round number
						print("Write out whole number")
				else:
					if ent.label_ == 'MONEY' and hasSign(text, startCheck): #if ending indicates text should be written and they used $
						print("Use numerals to represent this number")
					else: #they did not use $ but did not spell out round number
						print("Use numerals to represent this number and use $")
			#it seems spacy will not register these situations as MONEY but as cardinal			
			else: #two letters, negleting scenario where alpha starts and numeric ends, as unlikely
				if wholeGreaterThan(word):
					if ent.label_ == 'MONEY' and hasSign(text, startCheck): #This means they spell out word but don't use dollars
						print("use dollars in this instance")
				elif greaterThan(ent): #test to see if they are spelling out big number
					if ent.label_ == 'MONEY' and hasSign(text, startCheck):
						print("don't spell out number greater than 100")
					else:
						print("don't spell out number greater than 100 and use $ instead of dollars")
				elif ent.label_ == 'MONEY' and hasSign(text, startCheck):
					print("dollars should be used instead of $ for numbers less than or equal to 100")

		elif ent.label_ in {'QUANTITY', 'PERCENT'}: #then you want it to be numerals and not spelled out
			quantage(ent.label_, ent.text, ent.start_char, ent.end_char)




