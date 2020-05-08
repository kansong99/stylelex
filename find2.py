import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary.")

noun_count = 0;
for chunk in doc.noun_chunks:
  if chunk.root.dep_ == 'conj':
    noun_count = noun_count + 1
    comma_index = chunk[0].i - 2
  else:
    if noun_count > 1:
      print ("oxford comma at position", comma_index)
      noun_count = 0
if noun_count > 1:
    print ("oxford comma at position", comma_index)