import spacy
from difflib import SequenceMatcher
from . import links

#nlp = spacy.load("en_core_web_sm")
#doc = nlp("Aaron is a writer. Mr. Ansong is a coder. Aaron James Dang writes books and Kofi Ansong writes programs. Aarin and Mr. Anson are also entrepreneurs.")

def names_func(llist, option1 = None, option2 = None, option3 = None):

    #option1 - Full name on first reference (error 5)
    #option2 - Consistent shortened reference (error 3)
    #option3 - Check for misspelled names (error 7)

    names = [] # list to contain full names that previously appear in the doc
    for ent in llist.doc.ents:
        if ent.label_ == 'PERSON':
            error_index = ent.start_char
            full_name = ent.text.split() # creates list of names from named entity
            if not ent[-1].is_alpha: # removes suffixes like Jr. and Sr.
                del full_name[-1] 
            if len(full_name) >= 2: # name is not shortened (2 or more words)
                if (full_name in names): # checks if long name has not been used prior to this
# edit
                    flag1 = False
                    if option2 == True:
                        #print(ent.text, "-", "Position", ent[0].i, "-", "References following first usage of person's name should be shortened")
                        llist.insert(error_index, 3)
                else: 
                    flag1 = True 
                    for i in range(len(names)): # checks if extremely similar full names are found
                        if (SequenceMatcher(None, full_name, names[i]).ratio() > 0.7 and SequenceMatcher(None, full_name, names[i]).ratio() < 0.99):
# edit
                            if option3 == True:
                                #print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i], "\'? Consider using only surname.")
                                llist.insert(error_index, 3)
                            flag1 = False;
                            break
                    if flag1 == True: # if no other equivalent or similar names or are found
                        names.append(full_name)
            else: # name is shortened (1 word)
                flag2 = True
                flag3 = True
                for i in range(len(names)): # checks if shortened name has been used in full prior to this
                    if (full_name[0] == names[i][-1]) : # no error if last name
                        flag2 = False
                        flag3 = False
                        break
                    if (full_name[0] == names[i][0]) : # suggests usage of last name
# edit
                        if option2 == True:
                            #print (full_name, "-", "Position", ent[0].i, "-", "Consider using last name", "\'", names[i][-1], "\'.")
                            llist.insert(error_index, 3)
                        flag2 = False
                        flag3 = False
                        break
                if flag2: # checks if extremely similar first and last names are found
                    for i in range(len(names)):
                        if  (SequenceMatcher(None, full_name[0], names[i][0]).ratio() > 0.7 and SequenceMatcher(None, full_name[0], names[i][0]).ratio() < 0.99):
# edit
                            if option3 == True:
                                #print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i][0], "\'?")
                                llist.insert(error_index, 7)
                            flag3 = False
                            break
                        if  (SequenceMatcher(None, full_name[0], names[i][-1]).ratio() > 0.7 and SequenceMatcher(None, full_name[0], names[i][-1]).ratio() < 0.99):
# edit
                            if option3 == True:    
                                #print (full_name, "-", "Position", ent[0].i, "-", "Did you mean", "\'", names[i][-1], "\'?")
                                llist.insert(error_index, 7)
                            flag3 = False
                            break
                    if (flag3 == True): # if no other equivalent or similar names are found
# edit
                        if option1 == True:
                            #print (full_name, "-", "Position", ent[0].i, "-", "First usage of name should be full name.")
                            llist.insert(error_index, 5)
                        names.append(full_name)

#    print("names[] contains...", names)
