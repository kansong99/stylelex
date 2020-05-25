import spacy
from links import *


def find_func():
	noun_count = 0;
	for chunk in doc.noun_chunks:
	  if chunk.root.dep_ == 'conj':
	    noun_count = noun_count + 1
	    comma_index = chunk.start_char - 6
	  else:
	    if noun_count > 1:
	      llist.insert(comma_index, 1)
	      noun_count = 0
	if noun_count > 1:
	    llist.insert(comma_index, 1)
