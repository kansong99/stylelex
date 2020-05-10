import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Aaron is a writer. Mr. Ansong is a coder. Aaron James Dang writes books and Kofi Ansong writes programs. Aaron and Mr. Ansong are also entrepreneurs.")

names = [] # list to contain names that previously appear in the doc
for ent in doc.ents:
    if ent.label_ == 'PERSON': 
        full_name = ent.text.split() # creates list of names from named entity
        if not ent[-1].is_alpha: # removes suffixes like Jr. and Sr.
        	del full_name[-1]
        if len(full_name) >= 2: # if name is a full name, adds it to names[]
            for i in range(len(full_name)):
                if not (full_name[i] in names):
                    names.append(full_name[i])
        else:
            if not (full_name[0] in names): # if name is a single name, checks if it's in names[], then adds it to names[]
                print(ent.text, "-", "Position", ent[0].i, "-", "First usage of person's name should be a full name") # error if single name not in names[]
                names.append(full_name[0])

print("names[] contains...", names)