import spacy
from links import *



noun_count = 0;
for chunk in doc.noun_chunks:
  if chunk.root.dep_ == 'conj':
    noun_count = noun_count + 1
    comma_index = chunk[0].i - 2
  else:
    if noun_count > 1:
      print ("oxford comma at position", comma_index)
      llist.append
      noun_count = 0
if noun_count > 1:
    print ("oxford comma at position", comma_index)