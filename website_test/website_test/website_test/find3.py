import spacy
from links import *


def find_func(option):
	noun_count = 0;
	for chunk in llist.doc.noun_chunks:
		if chunk.root.dep_ == 'conj':
			noun_count = noun_count + 1
			comma_index = chunk.start_char - 6
		else:
			if noun_count > 1:
				if option == False and text[comma_index] == ",":
					llist.insert(comma_index, 1)
				if option == True and doc[token_index].text != ",":
					llist.insert(comma_index, 2)
					noun_count = 0
	if noun_count > 1:
		if option == False and text[comma_index] == ",":
			llist.insert(comma_index, 1)
		if option == True and doc[token_index].text != ",":
			llist.insert(comma_index, 2)
