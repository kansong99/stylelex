import spacy


nlp = spacy.load("en_core_web_md")

text = ("I went to the store, movies and park. I bought beer, hotdogs, and cheese. Afterwards, I met sally, Jill and Mary Tate and went on a run.")


doc = nlp(text)
#print(doc)
# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

#checker = {}

#an array that contains the final two words, where there should be a comma
final_two = []

#an array where we check all of the pairs in our second pass
oxfords = []

#simple switch to make sure we have adequate amount of conjs for an oxford comma
#  0 = nothing added, 1 = dummy added, 2 = append to oxford
bar = 0

for chunk in doc.noun_chunks: #first pass to identify all places for comma
    if chunk.root.dep_ == 'conj': #dependent noun
        if final_two == []: #this is the first conj, so we add conj as potential head
            final_two.append("dummy") #this is just to make the else clause consistent
            final_two.append(chunk.text)
            bar = 1
        
        else: #we have 3 or more words, so we need to check for potential oxford comma, set bar
            final_two.append(chunk.text)
            final_two.pop(0) #either dummy or extra word in list of nouns
            bar = 2

    elif bar == 2: #this means we have gotten to the end of a sequance of conjs we need to check here for comma and restore
        oxfords.append(final_two[:])
        final_two = []
        bar = 0
    
    elif bar == 1:
        final_two = []
        bar = 0

run = 0 # counter to run through doc
while oxfords:
    if oxfords[0][0] == doc[run].text: # and (doc[run + 2].text == oxfords[0][1] or doc[run + 3].text == oxfords[0][1]):
        if doc[run + 1].text == ",":
            print("oxford comma present between " + doc[run].text + " and " + doc[run + 3].text ) # + 3 to skip comma and word 'and'
        elif doc[run + 1].text == "and":
            print("oxford comma not present between " + doc[run].text + " and " + doc[run + 2].text)
        oxfords.pop(0)
    run += 1



#print(chunk.text, chunk.root.text,  chunk.root.dep_,
#        chunk.root.head.text)


