import spacy
from difflib import SequenceMatcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Aaron is a writer. Mr. Ansong is a coder. Aaron James Dang writes books and Kofi Ansong writes programs. Aarin and Mr. Anson are also entrepreneurs.")

names = [] # list to contain full names that previously appear in the doc
for ent in doc.ents:
    if ent.label_ == 'PERSON':
        full_name = ent.text.split() # creates list of names from named entity
        if not ent[-1].is_alpha: # removes suffixes like Jr. and Sr.
        	del full_name[-1] 
        if len(full_name) >= 2: # name is not shortened (2 or more words)
            if (full_name in names): # checks if long name has not been used prior to this
                print(ent.text, "-", "Position", ent[0].i, "-", "References following first usage of person's name should be shortened")
            else: 
                flag1 = True 
                for i in range(len(names)): # checks if extremely similar full names are found
                    if (SequenceMatcher(None, full_name, names[i]).ratio() > 0.7):
                        print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i], "\'? Consider using only surname.")
                        flag = False;
                        break
                if flag1: # if no other equivalent or similar names or are found
                    names.append(full_name)
        else: # name is shortened (1 word)
            flag2 = True
            flag3 = True
            for i in range(len(names)): # checks if shortened name has been used in full prior to this
                if (full_name == names[i][-1]) : # no error if last name
                    flag2 = False
                    flag3 = False
                    break
                if (full_name[0] == names[i][0]) : # suggests usage of last name
                    print (full_name, "-", "Position", ent[0].i, "-", "Consider using last name", "\'", names[i][-1], "\'.")
                    flag2 = False
                    flag3 = False
                    break
            if flag2: # checks if extremely similar first and last names are found
                for i in range(len(names)):
                    if  (SequenceMatcher(None, full_name[0], names[i][0]).ratio() > 0.7):
                        print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i][0], "\'?")
                        flag3 = False
                        break
                    if  (SequenceMatcher(None, full_name[0], names[i][-1]).ratio() > 0.7):
                        print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i][-1], "\'?")
                        flag3 = False
                        break
                if (flag3 == True): # if no other equivalent or similar names are found
                    print (full_name, "-", "Position", ent[0].i, "-", "First usage of name should be full name.")
                    names.append(full_name)

print("names[] contains...", names)
